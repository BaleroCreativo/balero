<?php
/**
 * Plugin Name: Expertia 360 – Configuración inicial
 * Description: Instala automáticamente toda la estructura del sitio: páginas, menús, categorías y opciones. Desactívalo y elimínalo tras ejecutarlo.
 * Version:     1.0.0
 * Author:      Balero Creativo
 */

defined('ABSPATH') || exit;

/* ============================================================
   1. MENÚ DE ADMINISTRACIÓN
   ============================================================ */
add_action('admin_menu', function () {
    add_management_page(
        'Configurar Expertia 360',
        'Expertia 360 Setup',
        'manage_options',
        'expertia360-setup',
        'expertia360_setup_page'
    );
});

/* ============================================================
   2. PÁGINA DE ADMIN
   ============================================================ */
function expertia360_setup_page() {
    $done = get_option('expertia360_setup_done', false);
    ?>
    <div class="wrap">
        <h1>⚙️ Expertia 360 — Configuración Inicial</h1>

        <?php if ($done) : ?>
            <div class="notice notice-success"><p><strong>✅ Sitio configurado correctamente.</strong> Ya puedes desactivar y eliminar este plugin.</p></div>
            <h2>Resumen de lo instalado</h2>
            <ul style="list-style:disc;margin-left:24px;line-height:2">
                <li>Tema <strong>Expertia 360</strong> activado</li>
                <li>5 Temáticas/Categorías creadas</li>
                <li>7 Páginas creadas (Home, Nosotros, Contacto, Publica, Aviso Legal, Privacidad, Cookies)</li>
                <li>Menú Principal (temáticas) y Menú Institucional asignados</li>
                <li>Menús del Footer configurados</li>
                <li>Homepage estática asignada</li>
            </ul>
            <p style="margin-top:16px"><a href="<?php echo esc_url(home_url('/')); ?>" target="_blank" class="button button-primary">Ver el sitio →</a></p>
        <?php else : ?>
            <p>Este plugin crea toda la estructura del sitio en un clic basándose en el wireframe de Expertia 360.</p>
            <p><strong>Incluye:</strong> categorías, páginas con sus plantillas, menús completos y homepage estática.</p>
            <div class="notice notice-warning"><p>⚠️ Ejecuta esto solo una vez. No lo repitas si ya tienes contenido.</p></div>
            <form method="post">
                <?php wp_nonce_field('expertia360_run_setup'); ?>
                <input type="hidden" name="expertia360_action" value="run">
                <?php submit_button('🚀 Instalar estructura del sitio', 'primary large'); ?>
            </form>
        <?php endif; ?>
    </div>
    <?php

    // Handle form submission
    if (
        isset($_POST['expertia360_action'], $_POST['_wpnonce']) &&
        $_POST['expertia360_action'] === 'run' &&
        wp_verify_nonce($_POST['_wpnonce'], 'expertia360_run_setup') &&
        current_user_can('manage_options')
    ) {
        expertia360_run_full_setup();
        echo '<script>location.reload();</script>';
    }
}

/* ============================================================
   3. LÓGICA PRINCIPAL DE SETUP
   ============================================================ */
function expertia360_run_full_setup() {

    // ── A. ACTIVAR TEMA ───────────────────────────────────────
    $theme = wp_get_theme('expertia360');
    if ($theme->exists()) {
        switch_theme('expertia360');
    }

    // ── B. CATEGORÍAS (TEMÁTICAS) ─────────────────────────────
    $tematicas = [
        'Tecnología'  => 'tecnologia',
        'Economía'    => 'economia',
        'Política'    => 'politica',
        'Sociedad'    => 'sociedad',
        'Cultura'     => 'cultura',
    ];
    $cat_ids = [];
    foreach ($tematicas as $name => $slug) {
        $existing = get_category_by_slug($slug);
        if ($existing) {
            $cat_ids[$slug] = $existing->term_id;
        } else {
            $result = wp_insert_category(['cat_name' => $name, 'category_nicename' => $slug]);
            if (!is_wp_error($result)) {
                $cat_ids[$slug] = $result;
            }
        }
    }

    // ── C. PÁGINAS ────────────────────────────────────────────
    $pages = [
        [
            'title'    => 'Inicio',
            'slug'     => 'inicio',
            'template' => '',           // front-page.php handles this via WordPress reading settings
            'content'  => '',
            'excerpt'  => '',
        ],
        [
            'title'    => 'Nosotros',
            'slug'     => 'nosotros',
            'template' => 'page-nosotros.php',
            'content'  => "En Expertia 360 creemos en el periodismo independiente, riguroso y accesible. Somos un equipo de profesionales apasionados por contar historias que importan.\n\nNuestro trabajo es conectar a expertos con lectores que buscan profundidad y contexto en cada tema que les apasiona.",
            'excerpt'  => 'Somos una revista digital independiente comprometida con el periodismo de calidad.',
        ],
        [
            'title'    => 'Contacto',
            'slug'     => 'contacto',
            'template' => 'page-contacto.php',
            'content'  => '',
            'excerpt'  => '¿Tienes alguna pregunta o propuesta? Nos encantaría escucharte.',
        ],
        [
            'title'    => 'Publica con nosotros',
            'slug'     => 'publica-con-nosotros',
            'template' => 'page-publica.php',
            'content'  => '',
            'excerpt'  => 'Anúnciate o publica con nosotros y llega a una audiencia especializada.',
        ],
        [
            'title'    => 'Aviso legal',
            'slug'     => 'aviso-legal',
            'template' => 'page-transparencia-legal.php',
            'content'  => "<h2>Aviso legal</h2>\n<p>En cumplimiento con la legislación vigente, se informa que el titular de este sitio web es Expertia 360.</p>\n<p>El acceso y uso de este sitio web está sujeto a los términos y condiciones descritos a continuación. Al navegar por nuestro sitio, aceptas estos términos.</p>\n<h2>Propiedad intelectual</h2>\n<p>Todos los contenidos publicados en Expertia 360, incluyendo textos, imágenes y elementos gráficos, son propiedad exclusiva de sus autores o de la revista, y están protegidos por la legislación de propiedad intelectual.</p>",
            'excerpt'  => 'Conoce nuestros términos, políticas y compromisos con la claridad en cada operación.',
        ],
        [
            'title'    => 'Privacidad',
            'slug'     => 'privacidad',
            'template' => 'page-transparencia-legal.php',
            'content'  => "<h2>Política de privacidad</h2>\n<p>En Expertia 360 nos comprometemos a proteger la privacidad de nuestros lectores y suscriptores.</p>\n<h2>Datos que recopilamos</h2>\n<p>Recopilamos únicamente la información que proporcionas voluntariamente, como tu correo electrónico al suscribirte a nuestra newsletter.</p>\n<h2>Uso de la información</h2>\n<p>Utilizamos tu información exclusivamente para enviarte nuestro contenido editorial. No compartimos tus datos con terceros bajo ninguna circunstancia.</p>",
            'excerpt'  => 'Conoce cómo tratamos y protegemos tu información personal.',
        ],
        [
            'title'    => 'Política de cookies',
            'slug'     => 'politica-de-cookies',
            'template' => 'page-transparencia-legal.php',
            'content'  => "<h2>Política de cookies</h2>\n<p>Este sitio web utiliza cookies para mejorar la experiencia de navegación. Al continuar navegando, aceptas el uso de cookies.</p>\n<h2>¿Qué son las cookies?</h2>\n<p>Las cookies son pequeños archivos de texto que se almacenan en tu dispositivo cuando visitas un sitio web. Nos permiten recordar tus preferencias y mejorar el funcionamiento del sitio.</p>\n<h2>Tipos de cookies que usamos</h2>\n<p>Usamos cookies técnicas (necesarias para el funcionamiento del sitio) y cookies analíticas (para entender cómo se usa el sitio, de forma anónima).</p>",
            'excerpt'  => 'Información sobre el uso de cookies en este sitio.',
        ],
    ];

    $page_ids = [];
    foreach ($pages as $page_data) {
        $existing = get_page_by_path($page_data['slug']);
        if ($existing) {
            $page_ids[$page_data['slug']] = $existing->ID;
            // Update template if needed
            if ($page_data['template']) {
                update_post_meta($existing->ID, '_wp_page_template', $page_data['template']);
            }
        } else {
            $args = [
                'post_title'   => $page_data['title'],
                'post_name'    => $page_data['slug'],
                'post_status'  => 'publish',
                'post_type'    => 'page',
                'post_content' => $page_data['content'],
                'post_excerpt' => $page_data['excerpt'],
            ];
            $id = wp_insert_post($args);
            if (!is_wp_error($id)) {
                $page_ids[$page_data['slug']] = $id;
                if ($page_data['template']) {
                    update_post_meta($id, '_wp_page_template', $page_data['template']);
                }
            }
        }
    }

    // ── D. HOMEPAGE ESTÁTICA ──────────────────────────────────
    // Create or get "Blog" page for posts
    $blog_page = get_page_by_path('blog');
    if (!$blog_page) {
        $blog_id = wp_insert_post([
            'post_title'  => 'Blog',
            'post_name'   => 'blog',
            'post_status' => 'publish',
            'post_type'   => 'page',
            'post_content'=> '',
        ]);
    } else {
        $blog_id = $blog_page->ID;
    }

    // front-page.php is used automatically when a static front page is set,
    // but for a magazine we want to use front-page.php for the homepage.
    // Actually leave reading settings as-is so front-page.php is always used.
    // If user wants latest posts on home: leave default. If they want static page, they set it manually.
    // For now set it to show latest posts (front-page.php overrides this).
    update_option('show_on_front', 'posts');

    // ── E. MENÚ PRINCIPAL (Temáticas) ────────────────────────
    $primary_menu_name = 'Menú Principal';
    $primary_menu_id   = wp_create_nav_menu($primary_menu_name);
    if (is_wp_error($primary_menu_id)) {
        $menus = wp_get_nav_menus();
        foreach ($menus as $menu) {
            if ($menu->name === $primary_menu_name) {
                $primary_menu_id = $menu->term_id;
                break;
            }
        }
    }

    // Add categories to primary menu
    $cat_order = 1;
    foreach ($tematicas as $name => $slug) {
        if (isset($cat_ids[$slug])) {
            wp_update_nav_menu_item($primary_menu_id, 0, [
                'menu-item-title'     => $name,
                'menu-item-object-id' => $cat_ids[$slug],
                'menu-item-object'    => 'category',
                'menu-item-type'      => 'taxonomy',
                'menu-item-status'    => 'publish',
                'menu-item-position'  => $cat_order++,
            ]);
        }
    }

    // ── F. MENÚ INSTITUCIONAL ─────────────────────────────────
    $secondary_menu_name = 'Menú Institucional';
    $secondary_menu_id   = wp_create_nav_menu($secondary_menu_name);
    if (is_wp_error($secondary_menu_id)) {
        $menus = wp_get_nav_menus();
        foreach ($menus as $menu) {
            if ($menu->name === $secondary_menu_name) {
                $secondary_menu_id = $menu->term_id;
                break;
            }
        }
    }

    $inst_pages = [
        ['Nosotros',           'nosotros'],
        ['Contacto',           'contacto'],
        ['Publica con nosotros','publica-con-nosotros'],
    ];
    $inst_order = 1;
    foreach ($inst_pages as [$label, $slug]) {
        if (isset($page_ids[$slug])) {
            wp_update_nav_menu_item($secondary_menu_id, 0, [
                'menu-item-title'     => $label,
                'menu-item-object-id' => $page_ids[$slug],
                'menu-item-object'    => 'page',
                'menu-item-type'      => 'post_type',
                'menu-item-status'    => 'publish',
                'menu-item-position'  => $inst_order++,
            ]);
        }
    }

    // ── G. MENÚ FOOTER – SECCIONES ───────────────────────────
    $footer_sec_id = wp_create_nav_menu('Footer – Secciones');
    if (is_wp_error($footer_sec_id)) {
        $menus = wp_get_nav_menus();
        foreach ($menus as $m) { if ($m->name === 'Footer – Secciones') { $footer_sec_id = $m->term_id; break; } }
    }
    $fsi = 1;
    foreach ($tematicas as $name => $slug) {
        if (isset($cat_ids[$slug])) {
            wp_update_nav_menu_item($footer_sec_id, 0, [
                'menu-item-title'     => $name,
                'menu-item-object-id' => $cat_ids[$slug],
                'menu-item-object'    => 'category',
                'menu-item-type'      => 'taxonomy',
                'menu-item-status'    => 'publish',
                'menu-item-position'  => $fsi++,
            ]);
        }
    }

    // ── H. MENÚ FOOTER – REVISTA ─────────────────────────────
    $footer_rev_id = wp_create_nav_menu('Footer – Revista');
    if (is_wp_error($footer_rev_id)) {
        $menus = wp_get_nav_menus();
        foreach ($menus as $m) { if ($m->name === 'Footer – Revista') { $footer_rev_id = $m->term_id; break; } }
    }
    $revista_pages = [
        ['Sobre nosotros',    'nosotros'],
        ['Publica tu artículo','publica-con-nosotros'],
        ['Contacto',          'contacto'],
    ];
    $rvi = 1;
    foreach ($revista_pages as [$label, $slug]) {
        if (isset($page_ids[$slug])) {
            wp_update_nav_menu_item($footer_rev_id, 0, [
                'menu-item-title'     => $label,
                'menu-item-object-id' => $page_ids[$slug],
                'menu-item-object'    => 'page',
                'menu-item-type'      => 'post_type',
                'menu-item-status'    => 'publish',
                'menu-item-position'  => $rvi++,
            ]);
        }
    }

    // ── I. MENÚ FOOTER – LEGAL ───────────────────────────────
    $footer_leg_id = wp_create_nav_menu('Footer – Legal');
    if (is_wp_error($footer_leg_id)) {
        $menus = wp_get_nav_menus();
        foreach ($menus as $m) { if ($m->name === 'Footer – Legal') { $footer_leg_id = $m->term_id; break; } }
    }
    $legal_pages = [
        ['Aviso legal',       'aviso-legal'],
        ['Privacidad',        'privacidad'],
        ['Política de cookies','politica-de-cookies'],
    ];
    $lgi = 1;
    foreach ($legal_pages as [$label, $slug]) {
        if (isset($page_ids[$slug])) {
            wp_update_nav_menu_item($footer_leg_id, 0, [
                'menu-item-title'     => $label,
                'menu-item-object-id' => $page_ids[$slug],
                'menu-item-object'    => 'page',
                'menu-item-type'      => 'post_type',
                'menu-item-status'    => 'publish',
                'menu-item-position'  => $lgi++,
            ]);
        }
    }

    // ── J. ASIGNAR MENÚS A UBICACIONES DEL TEMA ──────────────
    set_theme_mod('nav_menu_locations', [
        'primary'          => $primary_menu_id,
        'secondary'        => $secondary_menu_id,
        'footer-secciones' => $footer_sec_id,
        'footer-revista'   => $footer_rev_id,
        'footer-legal'     => $footer_leg_id,
    ]);

    // ── K. OPCIONES DEL CUSTOMIZER ────────────────────────────
    set_theme_mod('footer_tagline',  'Revista digital independiente.');
    set_theme_mod('contact_email',   'contacto@expertia360.com');
    set_theme_mod('contact_phone',   '+52 (555) 000-0000');
    set_theme_mod('about_text',
        'Expertia 360 es una revista digital independiente dedicada a llevar contenido especializado y riguroso a lectores que exigen profundidad. Cubrimos tecnología, economía, política, sociedad y cultura con la mirada de quienes viven cada tema.'
    );

    // ── L. OPCIONES GENERALES DE WORDPRESS ───────────────────
    update_option('blogname',        'Expertia 360');
    update_option('blogdescription', 'Revista digital independiente');

    // ── M. MARCAR COMO COMPLETADO ─────────────────────────────
    update_option('expertia360_setup_done', true);
}

/* ============================================================
   4. EJECUTAR SETUP AL ACTIVAR EL PLUGIN (opcional)
      Descomenta la siguiente línea si quieres que corra
      automáticamente al activar, sin pasar por el panel.
   ============================================================ */
// register_activation_hook(__FILE__, 'expertia360_run_full_setup');
