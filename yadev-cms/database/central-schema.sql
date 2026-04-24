-- ============================================================
-- YADEV CMS — CENTRAL DATABASE SCHEMA
-- DB name: yadev_central
-- MySQL 8.0+, utf8mb4, InnoDB
-- ============================================================
-- Esta DB vive en el VPS y contiene:
--   - Tenants (1 fila por cliente)
--   - Domains (mapping dominio → tenant)
--   - Users globales (super-admins YaDev)
--   - users_index (lookup cross-tenant email → tenant_id para login UX)
--   - Subscriptions (billing del tenant)
--   - Activity log cross-tenant (creación, suspensión, upgrades)
--   - Personal access tokens de super-admins
-- ============================================================

CREATE DATABASE IF NOT EXISTS `yadev_central`
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE `yadev_central`;

-- ------------------------------------------------------------
-- TENANTS
-- Cada cliente de YaDev es una fila aquí.
-- ------------------------------------------------------------
CREATE TABLE `tenants` (
  `id`          VARCHAR(191) NOT NULL COMMENT 'slug: multiservicios, ecomag, poron...',
  `name`        VARCHAR(191) NOT NULL COMMENT 'Multiservicios P&J S.A.S',
  `status`      ENUM('provisioning','active','suspended','deleted') NOT NULL DEFAULT 'provisioning',
  `plan`        ENUM('starter','standard','pro','enterprise') NOT NULL DEFAULT 'standard',
  `data`        JSON NULL COMMENT 'stancl/tenancy usa este campo genérico. settings extra.',
  `database`    VARCHAR(64) NOT NULL COMMENT 'nombre de la db: tenant_multiservicios',
  `industry`    VARCHAR(64) NULL COMMENT 'transporte, ambiental, construccion...',
  `primary_color` CHAR(7) NULL COMMENT '#0089D0',
  `logo_path`   VARCHAR(255) NULL,
  `onboarded_at` TIMESTAMP NULL,
  `suspended_at` TIMESTAMP NULL,
  `deleted_at`   TIMESTAMP NULL,
  `created_at`   TIMESTAMP NULL,
  `updated_at`   TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tenants_database_unique` (`database`),
  KEY `tenants_status_index` (`status`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- DOMAINS
-- Mapping 1-a-muchos: un tenant puede tener varios dominios.
-- Ejemplo: multiserviciospj.com + www.multiserviciospj.com + multiserviciospj.co
-- ------------------------------------------------------------
CREATE TABLE `domains` (
  `id`         BIGINT UNSIGNED AUTO_INCREMENT,
  `domain`     VARCHAR(255) NOT NULL,
  `tenant_id`  VARCHAR(191) NOT NULL,
  `is_primary` TINYINT(1) NOT NULL DEFAULT 0,
  `ssl_status` ENUM('pending','active','expired','error') DEFAULT 'pending',
  `created_at` TIMESTAMP NULL,
  `updated_at` TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domains_domain_unique` (`domain`),
  KEY `domains_tenant_id_foreign` (`tenant_id`),
  CONSTRAINT `domains_tenant_fk`
    FOREIGN KEY (`tenant_id`) REFERENCES `tenants` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- USERS (solo super-admins YaDev, vive en central)
-- Los usuarios DEL CLIENTE viven en la DB del tenant, no aquí.
-- ------------------------------------------------------------
CREATE TABLE `users` (
  `id`               BIGINT UNSIGNED AUTO_INCREMENT,
  `name`             VARCHAR(191) NOT NULL,
  `email`            VARCHAR(191) NOT NULL,
  `email_verified_at` TIMESTAMP NULL,
  `password`         VARCHAR(255) NOT NULL,
  `role`             ENUM('yadev_super_admin','yadev_staff') NOT NULL DEFAULT 'yadev_staff',
  `two_factor_secret` TEXT NULL,
  `two_factor_recovery_codes` TEXT NULL,
  `two_factor_confirmed_at` TIMESTAMP NULL,
  `remember_token`   VARCHAR(100) NULL,
  `last_login_at`    TIMESTAMP NULL,
  `last_login_ip`    VARCHAR(45) NULL,
  `created_at`       TIMESTAMP NULL,
  `updated_at`       TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_email_unique` (`email`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- USERS_INDEX
-- Lookup cross-tenant: dado un email, ¿en qué tenant vive?
-- Alimentado vía sync cuando se crea/borra usuario en un tenant.
-- Permite login UX sin preguntar "¿cuál es tu dominio?".
-- ------------------------------------------------------------
CREATE TABLE `users_index` (
  `id`         BIGINT UNSIGNED AUTO_INCREMENT,
  `email`      VARCHAR(191) NOT NULL,
  `tenant_id`  VARCHAR(191) NOT NULL,
  `user_id_in_tenant` BIGINT UNSIGNED NOT NULL COMMENT 'id del user dentro de la db del tenant',
  `created_at` TIMESTAMP NULL,
  `updated_at` TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_index_email_tenant_unique` (`email`, `tenant_id`),
  KEY `users_index_email_idx` (`email`),
  CONSTRAINT `users_index_tenant_fk`
    FOREIGN KEY (`tenant_id`) REFERENCES `tenants` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- SUBSCRIPTIONS (Billing del tenant)
-- Fase 2+: integración con pasarelas de pago (ePayco, Wompi).
-- ------------------------------------------------------------
CREATE TABLE `subscriptions` (
  `id`            BIGINT UNSIGNED AUTO_INCREMENT,
  `tenant_id`     VARCHAR(191) NOT NULL,
  `plan`          ENUM('starter','standard','pro','enterprise') NOT NULL,
  `status`        ENUM('trialing','active','past_due','canceled') NOT NULL DEFAULT 'active',
  `price_cop`     INT UNSIGNED NOT NULL COMMENT 'Precio mensual en pesos COP',
  `trial_ends_at` TIMESTAMP NULL,
  `current_period_start` TIMESTAMP NULL,
  `current_period_end`   TIMESTAMP NULL,
  `canceled_at`   TIMESTAMP NULL,
  `provider`      VARCHAR(32) NULL COMMENT 'epayco, wompi, manual',
  `provider_ref`  VARCHAR(128) NULL,
  `created_at`    TIMESTAMP NULL,
  `updated_at`    TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  KEY `subscriptions_tenant_id_idx` (`tenant_id`),
  CONSTRAINT `subscriptions_tenant_fk`
    FOREIGN KEY (`tenant_id`) REFERENCES `tenants` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- TENANT_ACTIVITY_LOG (cross-tenant audit para super-admin)
-- ------------------------------------------------------------
CREATE TABLE `tenant_activity_log` (
  `id`         BIGINT UNSIGNED AUTO_INCREMENT,
  `tenant_id`  VARCHAR(191) NULL,
  `actor_id`   BIGINT UNSIGNED NULL COMMENT 'FK a central.users',
  `actor_type` ENUM('system','super_admin','tenant_user') NOT NULL,
  `action`     VARCHAR(64) NOT NULL COMMENT 'tenant.created, tenant.suspended, impersonation.start...',
  `payload`    JSON NULL,
  `ip`         VARCHAR(45) NULL,
  `user_agent` TEXT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `tenant_activity_tenant_idx` (`tenant_id`),
  KEY `tenant_activity_action_idx` (`action`),
  KEY `tenant_activity_created_idx` (`created_at`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- PERSONAL_ACCESS_TOKENS (Sanctum) — solo para usuarios centrales
-- Los tokens de los usuarios del tenant viven en la DB del tenant.
-- ------------------------------------------------------------
CREATE TABLE `personal_access_tokens` (
  `id`             BIGINT UNSIGNED AUTO_INCREMENT,
  `tokenable_type` VARCHAR(255) NOT NULL,
  `tokenable_id`   BIGINT UNSIGNED NOT NULL,
  `name`           VARCHAR(255) NOT NULL,
  `token`          CHAR(64) NOT NULL,
  `abilities`      TEXT NULL,
  `last_used_at`   TIMESTAMP NULL,
  `expires_at`     TIMESTAMP NULL,
  `created_at`     TIMESTAMP NULL,
  `updated_at`     TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `personal_access_tokens_token_unique` (`token`),
  KEY `personal_access_tokens_tokenable_idx` (`tokenable_type`, `tokenable_id`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- PASSWORD_RESET_TOKENS
-- ------------------------------------------------------------
CREATE TABLE `password_reset_tokens` (
  `email`      VARCHAR(191) NOT NULL,
  `token`      VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- FAILED_JOBS (Horizon)
-- ------------------------------------------------------------
CREATE TABLE `failed_jobs` (
  `id`         BIGINT UNSIGNED AUTO_INCREMENT,
  `uuid`       VARCHAR(255) NOT NULL,
  `connection` TEXT NOT NULL,
  `queue`      TEXT NOT NULL,
  `payload`    LONGTEXT NOT NULL,
  `exception`  LONGTEXT NOT NULL,
  `failed_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `failed_jobs_uuid_unique` (`uuid`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- Seed inicial: super-admin Angel
-- Password será setteado con artisan después, aquí solo shape.
-- ------------------------------------------------------------
INSERT INTO `users` (`name`, `email`, `role`, `password`, `created_at`, `updated_at`) VALUES
('Angel', 'yadevsistem@gmail.com', 'yadev_super_admin', '$2y$12$PLACEHOLDER_BCRYPT', NOW(), NOW());

-- ============================================================
-- END central-schema.sql
-- ============================================================
