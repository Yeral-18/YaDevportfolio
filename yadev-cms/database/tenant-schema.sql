-- ============================================================
-- YADEV CMS — TENANT DATABASE SCHEMA (template)
-- Se aplica a cada DB `tenant_{slug}` (ej: tenant_multiservicios).
-- Creado automáticamente por `php artisan tenants:migrate`.
-- MySQL 8.0+, utf8mb4, InnoDB
-- ============================================================

-- ------------------------------------------------------------
-- USERS (usuarios del cliente)
-- Cada tenant tiene su propio pool de usuarios.
-- Email globalmente único vía central.users_index, pero el user
-- real vive aquí.
-- ------------------------------------------------------------
CREATE TABLE `users` (
  `id`               BIGINT UNSIGNED AUTO_INCREMENT,
  `name`             VARCHAR(191) NOT NULL,
  `email`            VARCHAR(191) NOT NULL,
  `email_verified_at` TIMESTAMP NULL,
  `password`         VARCHAR(255) NOT NULL,
  `phone`            VARCHAR(32) NULL,
  `avatar_path`      VARCHAR(255) NULL,
  `locale`           VARCHAR(8) NOT NULL DEFAULT 'es-CO',
  `remember_token`   VARCHAR(100) NULL,
  `last_login_at`    TIMESTAMP NULL,
  `last_login_ip`    VARCHAR(45) NULL,
  `created_at`       TIMESTAMP NULL,
  `updated_at`       TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_email_unique` (`email`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- ROLES & PERMISSIONS (spatie/laravel-permission)
-- ------------------------------------------------------------
CREATE TABLE `roles` (
  `id`         BIGINT UNSIGNED AUTO_INCREMENT,
  `name`       VARCHAR(191) NOT NULL,
  `guard_name` VARCHAR(191) NOT NULL DEFAULT 'web',
  `created_at` TIMESTAMP NULL,
  `updated_at` TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roles_name_guard_unique` (`name`, `guard_name`)
) ENGINE=InnoDB;

CREATE TABLE `permissions` (
  `id`         BIGINT UNSIGNED AUTO_INCREMENT,
  `name`       VARCHAR(191) NOT NULL,
  `guard_name` VARCHAR(191) NOT NULL DEFAULT 'web',
  `created_at` TIMESTAMP NULL,
  `updated_at` TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `permissions_name_guard_unique` (`name`, `guard_name`)
) ENGINE=InnoDB;

CREATE TABLE `model_has_roles` (
  `role_id`    BIGINT UNSIGNED NOT NULL,
  `model_type` VARCHAR(191) NOT NULL,
  `model_id`   BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (`role_id`, `model_id`, `model_type`),
  KEY `model_has_roles_model_idx` (`model_id`, `model_type`),
  CONSTRAINT `model_has_roles_role_fk` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE `model_has_permissions` (
  `permission_id` BIGINT UNSIGNED NOT NULL,
  `model_type`    VARCHAR(191) NOT NULL,
  `model_id`      BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (`permission_id`, `model_id`, `model_type`),
  KEY `model_has_permissions_model_idx` (`model_id`, `model_type`),
  CONSTRAINT `model_has_permissions_perm_fk` FOREIGN KEY (`permission_id`) REFERENCES `permissions` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE `role_has_permissions` (
  `permission_id` BIGINT UNSIGNED NOT NULL,
  `role_id`       BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (`permission_id`, `role_id`),
  CONSTRAINT `role_has_permissions_perm_fk` FOREIGN KEY (`permission_id`) REFERENCES `permissions` (`id`) ON DELETE CASCADE,
  CONSTRAINT `role_has_permissions_role_fk` FOREIGN KEY (`role_id`)       REFERENCES `roles` (`id`)       ON DELETE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- PAGES
-- Cada página del sitio del cliente.
-- ------------------------------------------------------------
CREATE TABLE `pages` (
  `id`          BIGINT UNSIGNED AUTO_INCREMENT,
  `parent_id`   BIGINT UNSIGNED NULL COMMENT 'para subpáginas',
  `slug`        VARCHAR(191) NOT NULL,
  `title`       VARCHAR(191) NOT NULL,
  `template`    VARCHAR(64) NOT NULL DEFAULT 'default' COMMENT 'home, service-detail, contact, custom',
  `status`      ENUM('draft','published','archived') NOT NULL DEFAULT 'draft',
  `is_home`     TINYINT(1) NOT NULL DEFAULT 0,
  `order`       INT NOT NULL DEFAULT 0,
  `visibility`  ENUM('public','private','members') NOT NULL DEFAULT 'public',
  `published_at` TIMESTAMP NULL,
  `created_by`  BIGINT UNSIGNED NULL,
  `updated_by`  BIGINT UNSIGNED NULL,
  `deleted_at`  TIMESTAMP NULL,
  `created_at`  TIMESTAMP NULL,
  `updated_at`  TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pages_slug_unique` (`slug`),
  KEY `pages_status_idx` (`status`),
  KEY `pages_parent_idx` (`parent_id`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- SECTIONS
-- Una página tiene múltiples secciones ordenadas.
-- ------------------------------------------------------------
CREATE TABLE `sections` (
  `id`         BIGINT UNSIGNED AUTO_INCREMENT,
  `page_id`    BIGINT UNSIGNED NOT NULL,
  `type`       VARCHAR(64) NOT NULL COMMENT 'hero, about, services, projects, contact, footer...',
  `order`      INT NOT NULL DEFAULT 0,
  `settings`   JSON NULL COMMENT 'spacing, bg color, etc.',
  `created_at` TIMESTAMP NULL,
  `updated_at` TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  KEY `sections_page_idx` (`page_id`, `order`),
  CONSTRAINT `sections_page_fk` FOREIGN KEY (`page_id`) REFERENCES `pages` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- BLOCKS
-- Contenido editable. `type` determina el schema de `data`.
-- ------------------------------------------------------------
CREATE TABLE `blocks` (
  `id`         BIGINT UNSIGNED AUTO_INCREMENT,
  `section_id` BIGINT UNSIGNED NOT NULL,
  `type`       VARCHAR(64) NOT NULL COMMENT 'hero_split, services_zigzag, rich_text, image_gallery...',
  `data`       JSON NOT NULL COMMENT 'Contenido validado contra schema por block type',
  `order`      INT NOT NULL DEFAULT 0,
  `version`    INT UNSIGNED NOT NULL DEFAULT 1,
  `is_visible` TINYINT(1) NOT NULL DEFAULT 1,
  `created_by` BIGINT UNSIGNED NULL,
  `updated_by` BIGINT UNSIGNED NULL,
  `deleted_at` TIMESTAMP NULL,
  `created_at` TIMESTAMP NULL,
  `updated_at` TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  KEY `blocks_section_idx` (`section_id`, `order`),
  KEY `blocks_type_idx` (`type`),
  CONSTRAINT `blocks_section_fk` FOREIGN KEY (`section_id`) REFERENCES `sections` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Historial de versiones de bloques (para rollback)
CREATE TABLE `block_versions` (
  `id`         BIGINT UNSIGNED AUTO_INCREMENT,
  `block_id`   BIGINT UNSIGNED NOT NULL,
  `version`    INT UNSIGNED NOT NULL,
  `data`       JSON NOT NULL,
  `actor_id`   BIGINT UNSIGNED NULL,
  `created_at` TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `block_versions_block_version_unique` (`block_id`, `version`),
  CONSTRAINT `block_versions_block_fk` FOREIGN KEY (`block_id`) REFERENCES `blocks` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- MEDIA (mediateca)
-- ------------------------------------------------------------
CREATE TABLE `media` (
  `id`          BIGINT UNSIGNED AUTO_INCREMENT,
  `folder`      VARCHAR(128) NULL,
  `file_name`   VARCHAR(255) NOT NULL,
  `disk`        VARCHAR(32) NOT NULL DEFAULT 'tenant-local',
  `path`        VARCHAR(500) NOT NULL COMMENT 'relativo al disco',
  `url`         VARCHAR(500) NOT NULL COMMENT 'URL pública completa',
  `mime_type`   VARCHAR(128) NOT NULL,
  `size`        BIGINT UNSIGNED NOT NULL COMMENT 'bytes',
  `width`       INT UNSIGNED NULL,
  `height`      INT UNSIGNED NULL,
  `alt`         VARCHAR(255) NULL,
  `title`       VARCHAR(255) NULL,
  `caption`     TEXT NULL,
  `thumbnails`  JSON NULL COMMENT '{ "thumb": "url", "medium": "url", "webp": "url" }',
  `hash`        CHAR(64) NULL COMMENT 'sha256 del contenido, dedup',
  `uploaded_by` BIGINT UNSIGNED NULL,
  `deleted_at`  TIMESTAMP NULL,
  `created_at`  TIMESTAMP NULL,
  `updated_at`  TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  KEY `media_folder_idx` (`folder`),
  KEY `media_hash_idx` (`hash`),
  KEY `media_mime_idx` (`mime_type`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- FORMS
-- ------------------------------------------------------------
CREATE TABLE `forms` (
  `id`           BIGINT UNSIGNED AUTO_INCREMENT,
  `slug`         VARCHAR(64) NOT NULL,
  `name`         VARCHAR(191) NOT NULL,
  `fields`       JSON NOT NULL COMMENT '[{name,label,type,required,options}]',
  `notifications` JSON NULL COMMENT '{email_to:[], whatsapp_to:"+57..."}',
  `recaptcha`    TINYINT(1) NOT NULL DEFAULT 1,
  `redirect_url` VARCHAR(255) NULL,
  `thank_you_text` TEXT NULL,
  `is_active`    TINYINT(1) NOT NULL DEFAULT 1,
  `created_at`   TIMESTAMP NULL,
  `updated_at`   TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `forms_slug_unique` (`slug`)
) ENGINE=InnoDB;

CREATE TABLE `form_submissions` (
  `id`         BIGINT UNSIGNED AUTO_INCREMENT,
  `form_id`    BIGINT UNSIGNED NOT NULL,
  `data`       JSON NOT NULL COMMENT 'snapshot de valores',
  `ip`         VARCHAR(45) NULL,
  `user_agent` TEXT NULL,
  `referrer`   VARCHAR(500) NULL,
  `utm_source` VARCHAR(128) NULL,
  `utm_medium` VARCHAR(128) NULL,
  `utm_campaign` VARCHAR(128) NULL,
  `is_spam`    TINYINT(1) NOT NULL DEFAULT 0,
  `read_at`    TIMESTAMP NULL,
  `archived_at` TIMESTAMP NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `form_submissions_form_idx` (`form_id`, `created_at`),
  KEY `form_submissions_read_idx` (`read_at`),
  CONSTRAINT `form_submissions_form_fk` FOREIGN KEY (`form_id`) REFERENCES `forms` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- POPUPS
-- ------------------------------------------------------------
CREATE TABLE `popups` (
  `id`           BIGINT UNSIGNED AUTO_INCREMENT,
  `name`         VARCHAR(191) NOT NULL,
  `content`      JSON NOT NULL COMMENT 'bloque tipo',
  `trigger_type` ENUM('time','scroll','exit_intent','click') NOT NULL,
  `trigger_value` VARCHAR(64) NULL COMMENT 'segundos, porcentaje, selector CSS',
  `target_pages` JSON NULL COMMENT 'array de page slugs o ["*"]',
  `target_devices` ENUM('all','desktop','mobile') NOT NULL DEFAULT 'all',
  `frequency`    ENUM('always','once_per_session','once_per_user') NOT NULL DEFAULT 'once_per_session',
  `active_from`  TIMESTAMP NULL,
  `active_until` TIMESTAMP NULL,
  `is_active`    TINYINT(1) NOT NULL DEFAULT 1,
  `views_count`  BIGINT UNSIGNED NOT NULL DEFAULT 0,
  `clicks_count` BIGINT UNSIGNED NOT NULL DEFAULT 0,
  `created_at`   TIMESTAMP NULL,
  `updated_at`   TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  KEY `popups_active_idx` (`is_active`, `active_from`, `active_until`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- MENUS
-- ------------------------------------------------------------
CREATE TABLE `menus` (
  `id`         BIGINT UNSIGNED AUTO_INCREMENT,
  `location`   VARCHAR(64) NOT NULL COMMENT 'header, footer, mobile',
  `name`       VARCHAR(191) NOT NULL,
  `created_at` TIMESTAMP NULL,
  `updated_at` TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `menus_location_unique` (`location`)
) ENGINE=InnoDB;

CREATE TABLE `menu_items` (
  `id`          BIGINT UNSIGNED AUTO_INCREMENT,
  `menu_id`     BIGINT UNSIGNED NOT NULL,
  `parent_id`   BIGINT UNSIGNED NULL,
  `label`       VARCHAR(128) NOT NULL,
  `href`        VARCHAR(500) NOT NULL,
  `link_type`   ENUM('page','external','anchor','custom') NOT NULL DEFAULT 'page',
  `target`      ENUM('_self','_blank') NOT NULL DEFAULT '_self',
  `order`       INT NOT NULL DEFAULT 0,
  `icon`        VARCHAR(64) NULL,
  `created_at`  TIMESTAMP NULL,
  `updated_at`  TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  KEY `menu_items_menu_idx` (`menu_id`, `order`),
  KEY `menu_items_parent_idx` (`parent_id`),
  CONSTRAINT `menu_items_menu_fk` FOREIGN KEY (`menu_id`) REFERENCES `menus` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- SETTINGS (key-value)
-- ------------------------------------------------------------
CREATE TABLE `settings` (
  `key`         VARCHAR(191) NOT NULL,
  `value`       JSON NOT NULL,
  `type`        VARCHAR(32) NOT NULL DEFAULT 'string' COMMENT 'string, number, boolean, json, media_id',
  `group`       VARCHAR(64) NOT NULL DEFAULT 'general' COMMENT 'general, seo, social, tracking, business',
  `updated_by`  BIGINT UNSIGNED NULL,
  `updated_at`  TIMESTAMP NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- SEO_META (por página)
-- ------------------------------------------------------------
CREATE TABLE `seo_meta` (
  `id`              BIGINT UNSIGNED AUTO_INCREMENT,
  `page_id`         BIGINT UNSIGNED NOT NULL,
  `meta_title`      VARCHAR(191) NULL,
  `meta_description` VARCHAR(500) NULL,
  `og_title`        VARCHAR(191) NULL,
  `og_description`  VARCHAR(500) NULL,
  `og_image_id`     BIGINT UNSIGNED NULL,
  `twitter_card`    VARCHAR(32) DEFAULT 'summary_large_image',
  `canonical_url`   VARCHAR(500) NULL,
  `robots`          VARCHAR(64) DEFAULT 'index, follow',
  `schema_jsonld`   JSON NULL COMMENT 'Schema.org editable por cliente',
  `keywords`        VARCHAR(500) NULL,
  `created_at`      TIMESTAMP NULL,
  `updated_at`      TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `seo_meta_page_unique` (`page_id`),
  CONSTRAINT `seo_meta_page_fk` FOREIGN KEY (`page_id`) REFERENCES `pages` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- REDIRECTS
-- ------------------------------------------------------------
CREATE TABLE `redirects` (
  `id`          BIGINT UNSIGNED AUTO_INCREMENT,
  `from_path`   VARCHAR(500) NOT NULL,
  `to_path`     VARCHAR(500) NOT NULL,
  `status_code` SMALLINT NOT NULL DEFAULT 301,
  `is_active`   TINYINT(1) NOT NULL DEFAULT 1,
  `hits`        BIGINT UNSIGNED NOT NULL DEFAULT 0,
  `created_at`  TIMESTAMP NULL,
  `updated_at`  TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `redirects_from_unique` (`from_path`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- TRANSLATIONS (Fase 3, i18n)
-- Reescrito en v3: shape estructurada (translated_blocks JSON)
-- en vez de row-per-field. Preserva estructura completa de
-- bloques cuando Claude traduce (Schema.org, alt text, URLs).
-- Ver architecture/api-contract.md y phases/phase-3-ai.md.
-- ------------------------------------------------------------
CREATE TABLE `translations` (
  `id`                 BIGINT UNSIGNED AUTO_INCREMENT,
  `page_id`            BIGINT UNSIGNED NOT NULL,
  `locale`             VARCHAR(8) NOT NULL COMMENT 'en, pt, fr...',
  `translated_blocks`  JSON NOT NULL COMMENT 'Array de blocks con data traducido, misma forma que blocks.data',
  `translated_slug`    VARCHAR(191) NULL COMMENT 'opcional: slug en idioma destino',
  `translated_seo`     JSON NULL COMMENT 'meta_title, meta_description, og_* traducidos',
  `ai_generated`       TINYINT(1) NOT NULL DEFAULT 0 COMMENT 'TRUE si vino de /ai/translate, FALSE si fue edición humana',
  `reviewed_by`        BIGINT UNSIGNED NULL,
  `reviewed_at`        TIMESTAMP NULL,
  `translated_at`      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_at`         TIMESTAMP NULL,
  `updated_at`         TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `translations_page_locale_unique` (`page_id`,`locale`),
  KEY `translations_locale_idx` (`locale`),
  CONSTRAINT `translations_page_fk` FOREIGN KEY (`page_id`) REFERENCES `pages` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- BRAND_VOICE (Fase 3, ADN comercial del tenant)
-- Inyectado como system prompt cacheable en toda llamada a IA.
-- Row única por tenant (no multi-row).
-- Ver phases/phase-3-ai.md semana 11.
-- ------------------------------------------------------------
CREATE TABLE `brand_voice` (
  `id`                BIGINT UNSIGNED AUTO_INCREMENT,
  `tone`              JSON NOT NULL COMMENT 'Array de tonos: ["profesional","cercano","autoritativo","tecnico","calido","aspiracional"]',
  `vocabulary_prefer` JSON NULL COMMENT 'Array de strings. Términos que la IA debe usar proactivamente.',
  `vocabulary_avoid`  JSON NULL COMMENT 'Array de strings. Términos prohibidos; la IA los evita y flaggea.',
  `sample_texts`      JSON NULL COMMENT 'Array [{label, text}] con 2-3 textos reales del cliente como few-shot examples',
  `industry_context`  TEXT NULL COMMENT 'Descripción industria y sector (ej: "Ingeniería civil y ambiental, sector petrolero Magdalena Medio")',
  `target_audience`   TEXT NULL COMMENT 'Perfil de audiencia (ej: "Gerentes de proyectos de Ecopetrol, Cenit, Terpel")',
  `updated_by`        BIGINT UNSIGNED NULL,
  `created_at`        TIMESTAMP NULL,
  `updated_at`        TIMESTAMP NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- SEO_AUDITS (Fase 3, resultados del auditor SEO/GEO)
-- Guarda cada auditoría ejecutada por el endpoint /ai/audit.
-- La UI del editor lee el audit más reciente por page_id.
-- Ver phases/phase-3-ai.md semana 12.
-- ------------------------------------------------------------
CREATE TABLE `seo_audits` (
  `id`               BIGINT UNSIGNED AUTO_INCREMENT,
  `page_id`          BIGINT UNSIGNED NOT NULL,
  `block_id`         BIGINT UNSIGNED NULL COMMENT 'NULL = audit de página completa, no-NULL = audit parcial de un bloque',
  `score_seo`        TINYINT UNSIGNED NOT NULL COMMENT '0-100',
  `score_geo`        TINYINT UNSIGNED NOT NULL COMMENT '0-100, Generative Engine Optimization',
  `score_overall`    TINYINT UNSIGNED NOT NULL,
  `grade`            VARCHAR(3) NOT NULL COMMENT 'A+, A, B+, B, C, D, F',
  `issues`           JSON NOT NULL COMMENT 'Array [{id, severity, category, message, field_path, suggestion}]',
  `suggestions_inline` JSON NULL COMMENT 'Sugerencias por block_id estructuradas',
  `model`            VARCHAR(64) NOT NULL COMMENT 'claude-haiku-4-5, claude-sonnet-4-6',
  `tokens_in`        INT UNSIGNED NOT NULL,
  `tokens_out`       INT UNSIGNED NOT NULL,
  `cache_hit_ratio`  DECIMAL(4,3) NULL COMMENT 'Porción de tokens servidos desde prompt cache',
  `cost_usd`         DECIMAL(10,6) NOT NULL DEFAULT 0,
  `audited_at`       TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `seo_audits_page_idx` (`page_id`, `audited_at`),
  KEY `seo_audits_block_idx` (`block_id`),
  KEY `seo_audits_score_idx` (`score_overall`),
  CONSTRAINT `seo_audits_page_fk` FOREIGN KEY (`page_id`) REFERENCES `pages` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- ANALYTICS_SNAPSHOTS (Fase 2, cache diario de GoAccess)
-- El cron parsea /var/log/nginx/{tenant}-access.log cada hora
-- y guarda snapshots diarios para dashboards rápidos.
-- Ver phases/phase-2-parity.md semana 9.5.
-- ------------------------------------------------------------
CREATE TABLE `analytics_snapshots` (
  `id`                   BIGINT UNSIGNED AUTO_INCREMENT,
  `date`                 DATE NOT NULL COMMENT 'Día cubierto por este snapshot',
  `visits_unique`        INT UNSIGNED NOT NULL DEFAULT 0,
  `pageviews`            INT UNSIGNED NOT NULL DEFAULT 0,
  `avg_visit_duration_sec` INT UNSIGNED NOT NULL DEFAULT 0,
  `bounce_rate`          DECIMAL(4,3) NOT NULL DEFAULT 0,
  `top_pages`            JSON NOT NULL COMMENT '[{path, views}]',
  `top_countries`        JSON NOT NULL COMMENT '[{code, name, visits}]',
  `top_browsers`         JSON NOT NULL COMMENT '[{name, share}]',
  `top_os`               JSON NOT NULL,
  `top_referrers`        JSON NOT NULL COMMENT '[{host, visits}]',
  `search_keywords`      JSON NULL COMMENT '[{term, visits}] — extraídos de Referer de Google/Bing',
  `hourly_heatmap`       JSON NOT NULL COMMENT 'matriz 7x24 visitas por día-de-semana × hora',
  `status_codes`         JSON NOT NULL COMMENT '{200: n, 404: n, 500: n, ...}',
  `created_at`           TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `analytics_snapshots_date_unique` (`date`),
  KEY `analytics_snapshots_created_idx` (`created_at`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- SEDES / SUCURSALES (Fase 2, gap Odir)
-- Entidad multi-sucursal. Consumida por bloques footer_mega,
-- contact_locations_map, page_contact.
-- Ver phases/phase-2-parity.md y architecture/api-contract.md.
-- ------------------------------------------------------------
CREATE TABLE `sedes` (
  `id`          BIGINT UNSIGNED AUTO_INCREMENT,
  `name`        VARCHAR(191) NOT NULL COMMENT 'ej: Sede Principal Barrancabermeja',
  `address`     VARCHAR(255) NOT NULL,
  `city`        VARCHAR(128) NOT NULL,
  `department`  VARCHAR(128) NULL COMMENT 'Santander, Cundinamarca...',
  `country`     CHAR(2) NOT NULL DEFAULT 'CO',
  `phone`       VARCHAR(32) NULL,
  `whatsapp`    VARCHAR(32) NULL,
  `email`       VARCHAR(191) NULL,
  `lat`         DECIMAL(10,7) NULL,
  `lng`         DECIMAL(10,7) NULL,
  `hours`       JSON NULL COMMENT '{mon_fri: "07:00-17:00", sat: "...", sun: "closed"}',
  `is_main`     TINYINT(1) NOT NULL DEFAULT 0,
  `order`       INT NOT NULL DEFAULT 0,
  `icon`        VARCHAR(64) NULL COMMENT 'lucide icon name',
  `photo_id`    BIGINT UNSIGNED NULL COMMENT 'FK opcional a media',
  `created_at`  TIMESTAMP NULL,
  `updated_at`  TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  KEY `sedes_order_idx` (`order`),
  KEY `sedes_is_main_idx` (`is_main`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- PUBLISHES (historial de rebuilds)
-- ------------------------------------------------------------
CREATE TABLE `publishes` (
  `id`          VARCHAR(40) NOT NULL COMMENT 'ulid: pub_xyz789',
  `actor_id`    BIGINT UNSIGNED NULL,
  `status`      ENUM('queued','building','deploying','success','failed','canceled') NOT NULL DEFAULT 'queued',
  `note`        VARCHAR(500) NULL,
  `started_at`  TIMESTAMP NULL,
  `finished_at` TIMESTAMP NULL,
  `duration_ms` INT UNSIGNED NULL,
  `commit_sha`  VARCHAR(40) NULL,
  `error_log`   MEDIUMTEXT NULL,
  `created_at`  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `publishes_status_idx` (`status`),
  KEY `publishes_created_idx` (`created_at`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- ACTIVITY_LOG (por tenant, granular)
-- ------------------------------------------------------------
CREATE TABLE `activity_log` (
  `id`           BIGINT UNSIGNED AUTO_INCREMENT,
  `actor_id`     BIGINT UNSIGNED NULL,
  `actor_name`   VARCHAR(191) NULL COMMENT 'snapshot por si el user se borra',
  `action`       VARCHAR(64) NOT NULL COMMENT 'block.updated, page.created, user.invited, publish.triggered',
  `subject_type` VARCHAR(64) NULL,
  `subject_id`   BIGINT UNSIGNED NULL,
  `before`       JSON NULL,
  `after`        JSON NULL,
  `ip`           VARCHAR(45) NULL,
  `user_agent`   TEXT NULL,
  `created_at`   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `activity_log_actor_idx` (`actor_id`),
  KEY `activity_log_subject_idx` (`subject_type`, `subject_id`),
  KEY `activity_log_action_idx` (`action`),
  KEY `activity_log_created_idx` (`created_at`)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- PERSONAL_ACCESS_TOKENS (Sanctum, por tenant)
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
-- PASSWORD_RESET_TOKENS (por tenant)
-- ------------------------------------------------------------
CREATE TABLE `password_reset_tokens` (
  `email`      VARCHAR(191) NOT NULL,
  `token`      VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB;

-- ============================================================
-- END tenant-schema.sql
-- ============================================================
