-- ============================================================
-- SEED — TENANT MULTISERVICIOS P&J
-- Se aplica a la DB `tenant_multiservicios` después de migrate.
-- Datos REALES extraídos de internal/PROYECTOS/2026/MULTISERVICIOS P&J/
-- ============================================================

USE `tenant_multiservicios`;

-- ------------------------------------------------------------
-- ROLES & PERMISSIONS
-- ------------------------------------------------------------
INSERT INTO `roles` (`name`, `guard_name`, `created_at`, `updated_at`) VALUES
('tenant_admin',  'web', NOW(), NOW()),
('tenant_editor', 'web', NOW(), NOW()),
('tenant_viewer', 'web', NOW(), NOW());

INSERT INTO `permissions` (`name`, `guard_name`, `created_at`, `updated_at`) VALUES
('pages.view', 'web', NOW(), NOW()),
('pages.create', 'web', NOW(), NOW()),
('pages.update', 'web', NOW(), NOW()),
('pages.delete', 'web', NOW(), NOW()),
('blocks.view', 'web', NOW(), NOW()),
('blocks.update', 'web', NOW(), NOW()),
('blocks.delete', 'web', NOW(), NOW()),
('media.view', 'web', NOW(), NOW()),
('media.upload', 'web', NOW(), NOW()),
('media.delete', 'web', NOW(), NOW()),
('forms.view', 'web', NOW(), NOW()),
('forms.submissions.read', 'web', NOW(), NOW()),
('forms.submissions.export', 'web', NOW(), NOW()),
('settings.view', 'web', NOW(), NOW()),
('settings.update', 'web', NOW(), NOW()),
('users.view', 'web', NOW(), NOW()),
('users.invite', 'web', NOW(), NOW()),
('users.update', 'web', NOW(), NOW()),
('site.publish', 'web', NOW(), NOW()),
('site.export', 'web', NOW(), NOW());

-- tenant_admin tiene todos los permisos
INSERT INTO `role_has_permissions` (`permission_id`, `role_id`)
SELECT p.id, r.id FROM `permissions` p CROSS JOIN `roles` r
WHERE r.name = 'tenant_admin';

-- tenant_editor: view + update (no delete, no publish, no users, no settings)
INSERT INTO `role_has_permissions` (`permission_id`, `role_id`)
SELECT p.id, r.id FROM `permissions` p CROSS JOIN `roles` r
WHERE r.name = 'tenant_editor'
  AND p.name IN ('pages.view','pages.update','blocks.view','blocks.update','media.view','media.upload','forms.view','forms.submissions.read');

-- tenant_viewer: solo .view
INSERT INTO `role_has_permissions` (`permission_id`, `role_id`)
SELECT p.id, r.id FROM `permissions` p CROSS JOIN `roles` r
WHERE r.name = 'tenant_viewer'
  AND p.name LIKE '%.view';

-- ------------------------------------------------------------
-- USERS
-- ------------------------------------------------------------
INSERT INTO `users` (`name`, `email`, `password`, `phone`, `created_at`, `updated_at`) VALUES
-- Password placeholder: bcrypt de 'CambiarEn1erLogin!' — se resetea en primer login
('Gerencia Multiservicios P&J', 'gerencia@multiserviciospj.com', '$2y$12$PLACEHOLDER_CHANGE_ON_FIRST_LOGIN', '+573204464553', NOW(), NOW());

-- Asignar rol tenant_admin
INSERT INTO `model_has_roles` (`role_id`, `model_type`, `model_id`)
SELECT r.id, 'App\\Models\\User', u.id FROM `roles` r, `users` u
WHERE r.name = 'tenant_admin' AND u.email = 'gerencia@multiserviciospj.com';

-- ------------------------------------------------------------
-- SETTINGS (datos de empresa)
-- ------------------------------------------------------------
INSERT INTO `settings` (`key`, `value`, `type`, `group`, `updated_at`) VALUES
('business.name',          JSON_QUOTE('MULTISERVICIOS P&J S.A.S'),           'string', 'business', NOW()),
('business.tagline',        JSON_QUOTE('Empresa de Ingeniería en Barrancabermeja'), 'string', 'business', NOW()),
('business.address',        JSON_QUOTE('Corregimiento El Llanito, Barrancabermeja, Santander, Colombia'), 'string', 'business', NOW()),
('business.city',           JSON_QUOTE('Barrancabermeja'),                   'string', 'business', NOW()),
('business.department',     JSON_QUOTE('Santander'),                          'string', 'business', NOW()),
('business.country',        JSON_QUOTE('Colombia'),                           'string', 'business', NOW()),
('business.phone',          JSON_QUOTE('+57 320 4464553'),                    'string', 'business', NOW()),
('business.phone_link',     JSON_QUOTE('+573204464553'),                      'string', 'business', NOW()),
('business.whatsapp',       JSON_QUOTE('+573204464553'),                      'string', 'business', NOW()),
('business.email',          JSON_QUOTE('gerencia@multiserviciospj.com'),      'string', 'business', NOW()),
('business.email_alt',      JSON_QUOTE('multiserviciospjsas@gmail.com'),      'string', 'business', NOW()),
('business.website',        JSON_QUOTE('https://www.multiserviciospj.com'),   'string', 'business', NOW()),
('business.industry',       JSON_QUOTE('Ingeniería civil, ambiental, transporte y energía'), 'string', 'business', NOW()),
('business.founded_year',   JSON_QUOTE('2015'),                               'string', 'business', NOW()),
('business.certifications', JSON_ARRAY('ISO 9001:2015','ISO 14001:2015','ISO 45001:2018'), 'json', 'business', NOW()),
-- Brand
('brand.primary_color',     JSON_QUOTE('#0089D0'),                            'string', 'brand', NOW()),
('brand.secondary_color',   JSON_QUOTE('#005B32'),                            'string', 'brand', NOW()),
('brand.accent_color',      JSON_QUOTE('#8CC63F'),                            'string', 'brand', NOW()),
('brand.font_display',      JSON_QUOTE('Plus Jakarta Sans'),                  'string', 'brand', NOW()),
('brand.font_body',         JSON_QUOTE('Inter'),                              'string', 'brand', NOW()),
-- SEO global
('seo.default_title_suffix', JSON_QUOTE(' | Multiservicios P&J'),             'string', 'seo', NOW()),
('seo.default_description', JSON_QUOTE('Transporte de carga, obras civiles, remediación ambiental e izaje en Barrancabermeja, Santander. Empresa certificada ISO 9001, 14001, 45001.'), 'string', 'seo', NOW()),
('seo.default_og_image',    JSON_QUOTE('/og-image.jpg'),                      'string', 'seo', NOW()),
('seo.robots',              JSON_QUOTE('index, follow'),                      'string', 'seo', NOW()),
-- Social
('social.facebook',         JSON_QUOTE(''),                                   'string', 'social', NOW()),
('social.instagram',        JSON_QUOTE(''),                                   'string', 'social', NOW()),
('social.linkedin',         JSON_QUOTE(''),                                   'string', 'social', NOW()),
-- Tracking
('tracking.ga4',            JSON_QUOTE(''),                                   'string', 'tracking', NOW()),
('tracking.meta_pixel',     JSON_QUOTE(''),                                   'string', 'tracking', NOW()),
-- reCAPTCHA
('recaptcha.site_key',      JSON_QUOTE(''),                                   'string', 'security', NOW()),
('recaptcha.secret_key',    JSON_QUOTE(''),                                   'string', 'security', NOW());

-- ------------------------------------------------------------
-- MENU (header)
-- ------------------------------------------------------------
INSERT INTO `menus` (`location`, `name`, `created_at`, `updated_at`) VALUES
('header', 'Menú Principal', NOW(), NOW()),
('footer-services', 'Servicios', NOW(), NOW());

SET @menu_header_id   = (SELECT id FROM menus WHERE location = 'header');
SET @menu_footer_id   = (SELECT id FROM menus WHERE location = 'footer-services');

INSERT INTO `menu_items` (`menu_id`, `label`, `href`, `link_type`, `order`, `created_at`, `updated_at`) VALUES
(@menu_header_id, 'Inicio',    '#inicio',    'anchor', 1, NOW(), NOW()),
(@menu_header_id, 'Nosotros',  '#nosotros',  'anchor', 2, NOW(), NOW()),
(@menu_header_id, 'Servicios', '#servicios', 'anchor', 3, NOW(), NOW()),
(@menu_header_id, 'Proyectos', '#proyectos', 'anchor', 4, NOW(), NOW()),
(@menu_header_id, 'Contacto',  '#contacto',  'anchor', 5, NOW(), NOW());

INSERT INTO `menu_items` (`menu_id`, `label`, `href`, `link_type`, `order`, `created_at`, `updated_at`) VALUES
(@menu_footer_id, 'Transporte de Carga',           '#servicios', 'anchor', 1, NOW(), NOW()),
(@menu_footer_id, 'Obras Civiles',                 '#servicios', 'anchor', 2, NOW(), NOW()),
(@menu_footer_id, 'Movimiento de Carga - Izaje',   '#servicios', 'anchor', 3, NOW(), NOW()),
(@menu_footer_id, 'Remediación Ambiental',         '#servicios', 'anchor', 4, NOW(), NOW()),
(@menu_footer_id, 'Transición Energética',         '#servicios', 'anchor', 5, NOW(), NOW()),
(@menu_footer_id, 'Alquiler de Maquinaria',        '#servicios', 'anchor', 6, NOW(), NOW());

-- ------------------------------------------------------------
-- PAGE: Home
-- ------------------------------------------------------------
INSERT INTO `pages` (`slug`, `title`, `template`, `status`, `is_home`, `order`, `published_at`, `created_at`, `updated_at`)
VALUES ('inicio', 'Inicio', 'home', 'published', 1, 0, NOW(), NOW(), NOW());
SET @page_home_id = LAST_INSERT_ID();

INSERT INTO `seo_meta` (`page_id`, `meta_title`, `meta_description`, `og_title`, `og_description`, `created_at`, `updated_at`) VALUES
(@page_home_id,
 'MULTISERVICIOS P&J S.A.S | Transporte de Carga, Obras Civiles y Remediación Ambiental en Barrancabermeja, Santander',
 'Transporte de carga, obras civiles, remediación ambiental e izaje en Barrancabermeja, Santander. Empresa certificada ISO 9001, 14001, 45001. Cotice ahora.',
 'MULTISERVICIOS P&J S.A.S',
 'Servicios integrales de ingeniería en Barrancabermeja y el Magdalena Medio.',
 NOW(), NOW());

-- ------------------------------------------------------------
-- SECTIONS + BLOCKS de Home
-- Orden: hero → about → services → benefits → clients → contact → footer
-- ------------------------------------------------------------

-- Section 1: HERO
INSERT INTO `sections` (`page_id`,`type`,`order`,`created_at`,`updated_at`)
VALUES (@page_home_id,'hero',1,NOW(),NOW());
SET @s_hero = LAST_INSERT_ID();

INSERT INTO `blocks` (`section_id`,`type`,`data`,`order`,`created_at`,`updated_at`) VALUES
(@s_hero, 'hero_split', JSON_OBJECT(
  'eyebrow',   'Empresa de Ingeniería en Barrancabermeja',
  'headline_parts', JSON_ARRAY(
    JSON_OBJECT('text','Transporte de Carga,','style','default'),
    JSON_OBJECT('text','Obras Civiles','style','accent'),
    JSON_OBJECT('text',' y Remediación Ambiental en Barrancabermeja','style','default')
  ),
  'description','Servicios integrales de transporte de carga, obras civiles, izaje de cargas, remediación ambiental y transición energética en Santander, Colombia. Empresa certificada ISO 9001, ISO 14001 e ISO 45001 con operaciones en Barrancabermeja y el Magdalena Medio.',
  'primary_cta',   JSON_OBJECT('label','Conocer Servicios','href','#servicios'),
  'secondary_cta', JSON_OBJECT('label','Contactar',          'href','#contacto'),
  'badges', JSON_ARRAY(
    JSON_OBJECT('label','Transporte',    'icon','building'),
    JSON_OBJECT('label','Ambiental',     'icon','leaf'),
    JSON_OBJECT('label','Energía Solar', 'icon','zap'),
    JSON_OBJECT('label','Obras Civiles', 'icon','cog')
  ),
  'background_style','gradient_dark_blue'
), 1, NOW(), NOW());

-- Section 2: STATS BAR
INSERT INTO `sections` (`page_id`,`type`,`order`,`created_at`,`updated_at`)
VALUES (@page_home_id,'stats',2,NOW(),NOW());
SET @s_stats = LAST_INSERT_ID();

INSERT INTO `blocks` (`section_id`,`type`,`data`,`order`,`created_at`,`updated_at`) VALUES
(@s_stats, 'stats_bar', JSON_OBJECT(
  'items', JSON_ARRAY(
    JSON_OBJECT('value',6,  'suffix','',  'label','Servicios Integrales'),
    JSON_OBJECT('value',3,  'suffix','',  'label','Certificaciones ISO'),
    JSON_OBJECT('value',4,  'suffix','+', 'label','Clientes en Santander'),
    JSON_OBJECT('value',10, 'suffix','+', 'label','Años de Experiencia')
  ),
  'background_style','gradient_blue'
), 1, NOW(), NOW());

-- Section 3: ABOUT (intro + mission/vision/values)
INSERT INTO `sections` (`page_id`,`type`,`order`,`created_at`,`updated_at`)
VALUES (@page_home_id,'about',3,NOW(),NOW());
SET @s_about = LAST_INSERT_ID();

INSERT INTO `blocks` (`section_id`,`type`,`data`,`order`,`created_at`,`updated_at`) VALUES
(@s_about, 'about_three_cards', JSON_OBJECT(
  'eyebrow','SOBRE NOSOTROS',
  'headline','Empresa de Ingeniería y Servicios Integrales en Barrancabermeja, Santander',
  'intro_html','<p><strong>MULTISERVICIOS P&amp;J S.A.S</strong> es una empresa de ingeniería ubicada en <strong>Barrancabermeja, corregimiento El Llanito, Santander, Colombia</strong>. Ofrecemos soluciones integrales en transporte de carga por carretera, alquiler de maquinaria pesada, remediación ambiental, obras civiles y transición energética para el Magdalena Medio y toda Colombia. Nuestro alcance abarca servicios de ingeniería civil, ambiental, eléctrica e industrial; ejecución de construcciones y mantenimiento locativo, gestión ambiental, tratamiento de aguas y residuos, consultoría técnica, instalación de paneles solares fotovoltaicos y fabricación de estructuras metálicas, todo certificado bajo los estándares ISO 9001, ISO 14001 e ISO 45001.</p>',
  'cards', JSON_ARRAY(
    JSON_OBJECT(
      'kind','mission',
      'title','Misión',
      'icon','target',
      'text','En Multiservicios P&J S.A.S., desde Barrancabermeja, Santander, ofrecemos soluciones integrales en transporte de carga, alquiler de maquinaria pesada, remediación ambiental y obras civiles para el sector de transición energética en Colombia. Nos comprometemos a prestar servicios de ingeniería de alta calidad, seguros y ambientalmente responsables, garantizando la satisfacción de nuestros clientes, el bienestar de nuestros colaboradores y el desarrollo sostenible del Magdalena Medio, bajo los estándares ISO 9001, ISO 14001 e ISO 45001.'
    ),
    JSON_OBJECT(
      'kind','vision',
      'title','Visión',
      'icon','eye',
      'text','Para el año 2030, seremos reconocidos a nivel nacional como la empresa líder en servicios integrales de ingeniería, transporte de carga y remediación ambiental en Santander y Colombia, destacando por nuestra excelencia operativa, innovación tecnológica y compromiso con la sostenibilidad. Buscamos expandir nuestro portafolio de obras civiles y transición energética, consolidar nuestra presencia desde Barrancabermeja hacia todo el territorio nacional y ser referente en calidad, seguridad y responsabilidad ambiental.'
    ),
    JSON_OBJECT(
      'kind','values',
      'title','Valores Corporativos',
      'icon','shield_check',
      'values', JSON_ARRAY(
        JSON_OBJECT('name','Excelencia y Calidad',                     'desc','Nos esforzamos continuamente por superar las expectativas de nuestros clientes y mejorar nuestros procesos, garantizando la máxima calidad en cada servicio que prestamos.'),
        JSON_OBJECT('name','Responsabilidad Ambiental e Innovación',   'desc','Actuamos con conciencia y respeto por el medio ambiente. Implementamos prácticas sostenibles en todas nuestras operaciones y contribuimos activamente a la remediación y protección de los ecosistemas.'),
        JSON_OBJECT('name','Seguridad y Bienestar',                    'desc','La seguridad de nuestros colaboradores y clientes es nuestra prioridad. Promovemos una cultura de cero accidentes y garantizamos entornos de trabajo seguros y saludables.')
      )
    )
  )
), 1, NOW(), NOW());

-- Section 4: SERVICES (zigzag)
INSERT INTO `sections` (`page_id`,`type`,`order`,`created_at`,`updated_at`)
VALUES (@page_home_id,'services',4,NOW(),NOW());
SET @s_services = LAST_INSERT_ID();

INSERT INTO `blocks` (`section_id`,`type`,`data`,`order`,`created_at`,`updated_at`) VALUES
(@s_services, 'services_zigzag', JSON_OBJECT(
  'eyebrow','NUESTROS SERVICIOS',
  'headline','Servicios Integrales de Ingeniería en Barrancabermeja y Colombia',
  'description','Ofrecemos un portafolio completo de servicios de transporte de carga, obras civiles, remediación ambiental y transición energética en Santander. Calidad, seguridad y sostenibilidad certificadas bajo ISO 9001, ISO 14001 e ISO 45001.',
  'items', JSON_ARRAY(
    JSON_OBJECT(
      'number','01',
      'title','Transporte de Carga por Carretera',
      'description','Servicio de transporte de carga por carretera en Barrancabermeja, Santander y toda Colombia. Contamos con una flota certificada para la movilización segura de equipos, materiales y maquinaria pesada para el sector energético e industrial.',
      'image_path','/images/services/transporte.jpg',
      'icon','truck'
    ),
    JSON_OBJECT(
      'number','02',
      'title','Obras Civiles y Mantenimiento Locativo',
      'description','Ejecución de obras civiles, construcción y mantenimiento locativo de edificaciones en Santander y el Magdalena Medio. Desarrollamos proyectos de infraestructura con los más altos estándares de calidad y seguridad certificada.',
      'image_path','/images/services/obras-civiles.jpg',
      'icon','building'
    ),
    JSON_OBJECT(
      'number','03',
      'title','Movimiento de Carga - Izaje',
      'description','Levantamiento de cargas pesadas con grúas y equipos certificados para proyectos industriales en Barrancabermeja y Colombia. Operaciones de izaje seguro y eficiente con personal capacitado y maquinaria especializada.',
      'image_path','/images/services/izaje.jpg',
      'icon','upload'
    ),
    JSON_OBJECT(
      'number','04',
      'title','Remediación Ambiental',
      'description','Servicios de remediación ambiental en Colombia: recuperación de cuerpos hídricos, restauración de ecosistemas, reforestación y retiro de material contaminante. Gestión ambiental integral certificada bajo ISO 14001 en Santander y el Magdalena Medio.',
      'image_path','/images/services/remediacion.jpg',
      'icon','leaf'
    ),
    JSON_OBJECT(
      'number','05',
      'title','Transición Energética',
      'description','Instalación de paneles solares fotovoltaicos y soluciones de energía renovable en Colombia. Impulsamos la transición energética empresarial con proyectos sostenibles que reducen costos operativos y la huella de carbono.',
      'image_path','/images/services/transicion-energetica.jpg',
      'icon','sun'
    ),
    JSON_OBJECT(
      'number','06',
      'title','Alquiler de Maquinaria',
      'description','Alquiler de maquinaria pesada y equipos de construcción en Barrancabermeja y Santander. Disponemos de retroexcavadoras, volquetas, grúas y equipos especializados para proyectos de infraestructura y operaciones industriales.',
      'image_path','/images/services/maquinaria.jpg',
      'icon','tools'
    )
  ),
  'cta_label','Solicitar cotización',
  'cta_href','#contacto'
), 1, NOW(), NOW());

-- Section 5: BENEFITS
INSERT INTO `sections` (`page_id`,`type`,`order`,`created_at`,`updated_at`)
VALUES (@page_home_id,'benefits',5,NOW(),NOW());
SET @s_benefits = LAST_INSERT_ID();

INSERT INTO `blocks` (`section_id`,`type`,`data`,`order`,`created_at`,`updated_at`) VALUES
(@s_benefits, 'benefits_grid', JSON_OBJECT(
  'eyebrow','¿POR QUÉ ELEGIRNOS?',
  'headline','Razones para Confiar en Multiservicios P&J en Barrancabermeja',
  'description','Más de una década de experiencia en Santander respaldan nuestro compromiso con la excelencia en obras civiles, transporte de carga y remediación ambiental en cada proyecto.',
  'items', JSON_ARRAY(
    JSON_OBJECT(
      'title','Solución Integral en un Solo Proveedor',
      'description','En Barrancabermeja y Santander, ofrecemos todos los servicios que necesita en un solo lugar: transporte de carga, obras civiles, remediación ambiental, izaje de cargas pesadas y transición energética.',
      'icon','hub'
    ),
    JSON_OBJECT(
      'title','Calidad Certificada ISO en Cada Proyecto',
      'description','Trabajamos bajo los más altos estándares internacionales con certificaciones ISO 9001, ISO 14001 e ISO 45001, garantizando excelencia en cada obra civil, transporte y operación ambiental en Colombia.',
      'icon','award'
    ),
    JSON_OBJECT(
      'title','Líderes en Transición Energética',
      'description','Lideramos la instalación de paneles solares fotovoltaicos y prácticas sostenibles en Barrancabermeja y el Magdalena Medio, contribuyendo al desarrollo de energía renovable en Colombia.',
      'icon','sun'
    )
  )
), 1, NOW(), NOW());

-- Section 6: PROJECTS (bento)
INSERT INTO `sections` (`page_id`,`type`,`order`,`created_at`,`updated_at`)
VALUES (@page_home_id,'projects',6,NOW(),NOW());
SET @s_projects = LAST_INSERT_ID();

INSERT INTO `blocks` (`section_id`,`type`,`data`,`order`,`created_at`,`updated_at`) VALUES
(@s_projects, 'bento_projects', JSON_OBJECT(
  'eyebrow','NUESTROS CLIENTES',
  'headline','Clientes que Confían en Nosotros',
  'featured', JSON_OBJECT(
    'title','UTCMM2',
    'category','Izaje & Transporte',
    'description','Movimiento de cargas, izaje, transporte y alquiler de maquinaria para proyectos de gran escala en el sector de transición energética.',
    'location','Barrancabermeja, Colombia',
    'image_path','/images/services/izaje.jpg',
    'badge_color','#0089D0'
  ),
  'items', JSON_ARRAY(
    JSON_OBJECT('title','Impulsa Social S.A.S',   'category','Transporte de Carga',     'description','Transporte de carga por carretera, movilización de equipos y logística integral para operaciones del sector energético.', 'image_path','/images/projects/transporte-proyecto.jpg', 'badge_color','#0089D0'),
    JSON_OBJECT('title','Ecomag S.A.S',           'category','Remediación Ambiental',   'description','Reforestación y remediación ambiental. Recuperación de cuerpos hídricos y ecosistemas a través de prácticas sostenibles.', 'image_path','/images/projects/ambiental-proyecto.jpg', 'badge_color','#2E7D32'),
    JSON_OBJECT('title','Construagro Colombia S.A.S', 'category','Alquiler de Maquinaria', 'description','Alquiler de maquinaria pesada y equipos especializados para proyectos de construcción e infraestructura.', 'image_path','/images/projects/maquinaria-proyecto.jpg', 'badge_color','#0089D0')
  )
), 1, NOW(), NOW());

-- Section 7: CLIENTS (carousel)
INSERT INTO `sections` (`page_id`,`type`,`order`,`created_at`,`updated_at`)
VALUES (@page_home_id,'clients',7,NOW(),NOW());
SET @s_clients = LAST_INSERT_ID();

INSERT INTO `blocks` (`section_id`,`type`,`data`,`order`,`created_at`,`updated_at`) VALUES
(@s_clients, 'clients_carousel', JSON_OBJECT(
  'eyebrow','Nuestros Aliados',
  'headline','Clientes que Confían en Nosotros',
  'description','Empresas líderes del sector energético y de infraestructura en Colombia confían en nuestros servicios integrales.',
  'items', JSON_ARRAY(
    JSON_OBJECT('name','Impulsa Social S.A.S','industry','Transporte de carga por carretera','logo_path','/images/clients/impulsa-social.png'),
    JSON_OBJECT('name','UTCMM2','industry','Movimiento de cargas, Izaje, Transporte y Alquiler de Maquinaria','logo_path','/images/clients/utcmm2.png'),
    JSON_OBJECT('name','Ecomag S.A.S','industry','Reforestación y Remediación Ambiental','logo_path','/images/clients/ecomag-logo.png'),
    JSON_OBJECT('name','Construagro Colombia S.A.S','industry','Alquiler de Maquinaria','logo_path','/images/clients/construagro.png'),
    JSON_OBJECT('name','Construcciones, Consultoría y Montajes J.R.S S.A.S','industry','Construcción e Infraestructura','logo_path','/images/clients/construcciones-jrs.png')
  )
), 1, NOW(), NOW());

-- Section 8: CONTACT
INSERT INTO `sections` (`page_id`,`type`,`order`,`created_at`,`updated_at`)
VALUES (@page_home_id,'contact',8,NOW(),NOW());
SET @s_contact = LAST_INSERT_ID();

-- Primero el form
INSERT INTO `forms` (`slug`,`name`,`fields`,`notifications`,`recaptcha`,`thank_you_text`,`is_active`,`created_at`,`updated_at`) VALUES
('contacto-principal', 'Contacto Principal',
 JSON_ARRAY(
   JSON_OBJECT('name','nombre',   'label','Nombre Completo',    'type','text',     'required',true),
   JSON_OBJECT('name','email',    'label','Correo Electrónico', 'type','email',    'required',true),
   JSON_OBJECT('name','telefono', 'label','Teléfono',           'type','tel',      'required',true),
   JSON_OBJECT('name','servicio', 'label','Servicio de Interés','type','select',   'required',true, 'options', JSON_ARRAY(
      'Transporte de Carga por Carretera',
      'Obras Civiles y Mantenimiento Locativo',
      'Movimiento de Carga - Izaje',
      'Remediación Ambiental',
      'Transición Energética',
      'Alquiler de Maquinaria'
   )),
   JSON_OBJECT('name','mensaje',  'label','Mensaje',            'type','textarea', 'required',false)
 ),
 JSON_OBJECT('email_to', JSON_ARRAY('gerencia@multiserviciospj.com'), 'whatsapp_to','+573204464553'),
 1,
 'Su consulta fue enviada correctamente. Nuestro equipo le responderá a la brevedad.',
 1, NOW(), NOW());
SET @form_id = LAST_INSERT_ID();

INSERT INTO `blocks` (`section_id`,`type`,`data`,`order`,`created_at`,`updated_at`) VALUES
(@s_contact, 'contact_form', JSON_OBJECT(
  'eyebrow','CONTÁCTENOS',
  'headline','¿Tiene un Proyecto en Mente?',
  'description','Cuéntenos sobre su proyecto y nuestro equipo de ingenieros le brindará una asesoría personalizada sin compromiso.',
  'form_id',@form_id,
  'info_cards', JSON_ARRAY(
    JSON_OBJECT('icon','phone',   'title','Teléfono','value','+57 320 4464553',                 'href','tel:+573204464553'),
    JSON_OBJECT('icon','mail',    'title','Correo',  'value','multiserviciospjsas@gmail.com',  'href','mailto:multiserviciospjsas@gmail.com'),
    JSON_OBJECT('icon','map_pin', 'title','Oficina', 'value','Barrancabermeja, Corregimiento El Llanito', 'href',NULL)
  ),
  'buttons', JSON_ARRAY(
    JSON_OBJECT('type','email',    'label','Enviar por Correo',   'primary',true),
    JSON_OBJECT('type','whatsapp', 'label','Enviar por WhatsApp', 'primary',false)
  )
), 1, NOW(), NOW());

-- Section 9: FOOTER
INSERT INTO `sections` (`page_id`,`type`,`order`,`created_at`,`updated_at`)
VALUES (@page_home_id,'footer',9,NOW(),NOW());
SET @s_footer = LAST_INSERT_ID();

-- CTA Banner + Footer (un solo bloque compuesto)
INSERT INTO `blocks` (`section_id`,`type`,`data`,`order`,`created_at`,`updated_at`) VALUES
(@s_footer, 'cta_banner', JSON_OBJECT(
  'headline','¿Listo para su próximo proyecto?',
  'description','Contáctenos hoy para una cotización sin compromiso',
  'cta', JSON_OBJECT('label','Solicitar Cotización','href','#contacto'),
  'style','gradient_blue'
), 1, NOW(), NOW()),

(@s_footer, 'footer_mega', JSON_OBJECT(
  'tagline','Empresa de ingeniería en Barrancabermeja, Santander. Soluciones integrales en transporte de carga, obras civiles, remediación ambiental y transición energética en Colombia.',
  'social', JSON_ARRAY(
    JSON_OBJECT('platform','facebook', 'url','#'),
    JSON_OBJECT('platform','instagram','url','#'),
    JSON_OBJECT('platform','linkedin', 'url','#'),
    JSON_OBJECT('platform','whatsapp', 'url','https://wa.me/573204464553')
  ),
  'services_menu_location','footer-services',
  'contact_block', JSON_OBJECT(
    'address','Corregimiento El Llanito, Barrancabermeja, Santander, Colombia',
    'phone','+57 320 4464553',
    'email','gerencia@multiserviciospj.com',
    'website','https://www.multiserviciospj.com'
  ),
  'certifications_image','/images/bureau-veritas-iso.png',
  'copyright_text','© 2026 MULTISERVICIOS P&J S.A.S. Todos los derechos reservados.',
  'made_in','Hecho con ❤ en Colombia'
), 2, NOW(), NOW());

-- ------------------------------------------------------------
-- Activity log: seed
-- ------------------------------------------------------------
INSERT INTO `activity_log` (`actor_id`,`actor_name`,`action`,`subject_type`,`subject_id`,`created_at`) VALUES
(NULL, 'System (seed)', 'tenant.seeded', 'tenant', NULL, NOW());

-- ============================================================
-- END seed-multiservicios.sql
-- ============================================================
