<?php
defined('ABSPATH') || exit;

/* ----------------------------------------------------------
   THEME SETUP
   ---------------------------------------------------------- */
function expertia360_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('automatic-feed-links');
    add_theme_support('html5', ['search-form','comment-form','comment-list','gallery','caption','style','script']);
    add_theme_support('custom-logo', ['width' => 300, 'height' => 100]);
    add_theme_support('editor-styles');

    add_image_size('expertia-hero',     1200, 630,  true);
    add_image_size('expertia-card',     600,  450,  true);
    add_image_size('expertia-featured', 1400, 600,  true);
    add_image_size('expertia-sidebar',  400,  300,  true);

    register_nav_menus([
        'primary'   => __('Menú Principal (Temáticas)',        'expertia360'),
        'secondary' => __('Menú Institucional (Nosotros/...)', 'expertia360'),
        'footer-secciones' => __('Footer – Secciones',         'expertia360'),
        'footer-revista'   => __('Footer – Revista',           'expertia360'),
        'footer-legal'     => __('Footer – Legal',             'expertia360'),
    ]);

    load_theme_textdomain('expertia360', get_template_directory() . '/languages');
}
add_action('after_setup_theme', 'expertia360_setup');

/* ----------------------------------------------------------
   ENQUEUE
   ---------------------------------------------------------- */
function expertia360_enqueue() {
    wp_enqueue_style(
        'dancing-script',
        'https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap',
        [],
        null
    );

    wp_enqueue_style(
        'expertia360-style',
        get_stylesheet_uri(),
        ['dancing-script'],
        wp_get_theme()->get('Version')
    );

    wp_enqueue_script(
        'expertia360-main',
        get_template_directory_uri() . '/assets/js/main.js',
        [],
        wp_get_theme()->get('Version'),
        true
    );

    wp_localize_script('expertia360-main', 'expertia360', [
        'ajaxUrl' => admin_url('admin-ajax.php'),
        'nonce'   => wp_create_nonce('expertia360_nonce'),
    ]);
}
add_action('wp_enqueue_scripts', 'expertia360_enqueue');

/* ----------------------------------------------------------
   READING TIME
   ---------------------------------------------------------- */
function expertia360_reading_time($post_id = null) {
    $content    = get_post_field('post_content', $post_id ?: get_the_ID());
    $word_count = str_word_count(strip_tags($content));
    $minutes    = max(1, (int) ceil($word_count / 200));
    return $minutes . ' MIN';
}

/* ----------------------------------------------------------
   PLACEHOLDER SVG
   ---------------------------------------------------------- */
function expertia360_placeholder_svg($class = 'img-placeholder') {
    return '<div class="' . esc_attr($class) . '" aria-hidden="true">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
        </svg>
    </div>';
}

/* ----------------------------------------------------------
   THUMBNAIL HELPER
   ---------------------------------------------------------- */
function expertia360_thumbnail($size = 'expertia-card', $class = '', $placeholder_class = 'img-placeholder') {
    if (has_post_thumbnail()) {
        echo '<div class="' . esc_attr($placeholder_class) . '-wrap">';
        the_post_thumbnail($size, ['class' => esc_attr($class), 'loading' => 'lazy']);
        echo '</div>';
    } else {
        echo expertia360_placeholder_svg($placeholder_class);
    }
}

/* ----------------------------------------------------------
   SOCIAL LINKS (configured as theme mod)
   ---------------------------------------------------------- */
function expertia360_social_links() {
    $links = [
        'facebook'  => ['url' => get_theme_mod('social_facebook',  ''), 'label' => 'Facebook',  'svg' => '<path d="M24 12.07C24 5.41 18.63 0 12 0S0 5.41 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.04V9.41c0-3.02 1.8-4.7 4.54-4.7 1.31 0 2.68.24 2.68.24v2.97h-1.5c-1.5 0-1.96.93-1.96 1.89v2.26h3.32l-.53 3.49h-2.79V24C19.62 23.1 24 18.1 24 12.07z"/>'],
        'instagram' => ['url' => get_theme_mod('social_instagram', ''), 'label' => 'Instagram', 'svg' => '<path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/>'],
        'linkedin'  => ['url' => get_theme_mod('social_linkedin',  ''), 'label' => 'LinkedIn',  'svg' => '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>'],
    ];

    echo '<div class="social-links">';
    foreach ($links as $key => $link) {
        if (!empty($link['url'])) {
            printf(
                '<a href="%s" target="_blank" rel="noopener noreferrer" aria-label="%s"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">%s</svg></a>',
                esc_url($link['url']),
                esc_attr($link['label']),
                $link['svg']
            );
        }
    }
    echo '</div>';
}

/* ----------------------------------------------------------
   EXCERPT LENGTH
   ---------------------------------------------------------- */
add_filter('excerpt_length', fn() => 25, 999);
add_filter('excerpt_more',   fn() => '…');

/* ----------------------------------------------------------
   NEWSLETTER FORM HANDLER
   ---------------------------------------------------------- */
function expertia360_handle_newsletter() {
    if (empty($_POST['newsletter_email']) || empty($_POST['_wpnonce'])) {
        wp_redirect(add_query_arg('nl', 'error', wp_get_referer()));
        exit;
    }

    if (!wp_verify_nonce($_POST['_wpnonce'], 'expertia360_newsletter')) {
        wp_redirect(add_query_arg('nl', 'error', wp_get_referer()));
        exit;
    }

    $email = sanitize_email($_POST['newsletter_email']);
    if (!is_email($email)) {
        wp_redirect(add_query_arg('nl', 'invalid', wp_get_referer()));
        exit;
    }

    // Save subscriber as WP option list (simple storage; replace with Mailchimp API later)
    $subscribers = get_option('expertia360_subscribers', []);
    if (!in_array($email, $subscribers, true)) {
        $subscribers[] = $email;
        update_option('expertia360_subscribers', $subscribers, false);
    }

    // Notify admin
    $admin_email = get_option('admin_email');
    wp_mail($admin_email, 'Nuevo suscriptor – Expertia 360', "Correo: {$email}");

    wp_redirect(add_query_arg('nl', 'ok', wp_get_referer()));
    exit;
}
add_action('admin_post_nopriv_expertia360_newsletter', 'expertia360_handle_newsletter');
add_action('admin_post_expertia360_newsletter',        'expertia360_handle_newsletter');

/* ----------------------------------------------------------
   CONTACT FORM HANDLER
   ---------------------------------------------------------- */
function expertia360_handle_contact() {
    if (empty($_POST['_wpnonce']) || !wp_verify_nonce($_POST['_wpnonce'], 'expertia360_contact')) {
        wp_redirect(add_query_arg('cf', 'error', wp_get_referer()));
        exit;
    }

    $name    = sanitize_text_field($_POST['contact_name']    ?? '');
    $email   = sanitize_email($_POST['contact_email']        ?? '');
    $phone   = sanitize_text_field($_POST['contact_phone']   ?? '');
    $message = sanitize_textarea_field($_POST['contact_message'] ?? '');

    if (!$name || !is_email($email) || !$message) {
        wp_redirect(add_query_arg('cf', 'invalid', wp_get_referer()));
        exit;
    }

    $admin_email = get_option('admin_email');
    $subject     = 'Nuevo mensaje de contacto – Expertia 360';
    $body        = "Nombre: {$name}\nCorreo: {$email}\nTeléfono: {$phone}\n\nMensaje:\n{$message}";
    $headers     = ["Reply-To: {$name} <{$email}>", 'Content-Type: text/plain; charset=UTF-8'];

    wp_mail($admin_email, $subject, $body, $headers);

    wp_redirect(add_query_arg('cf', 'ok', wp_get_referer()));
    exit;
}
add_action('admin_post_nopriv_expertia360_contact', 'expertia360_handle_contact');
add_action('admin_post_expertia360_contact',        'expertia360_handle_contact');

/* ----------------------------------------------------------
   CUSTOMIZER: Social Links & About Text
   ---------------------------------------------------------- */
function expertia360_customizer($wp_customize) {
    $wp_customize->add_section('expertia360_social', [
        'title'    => 'Redes Sociales',
        'priority' => 130,
    ]);
    foreach (['facebook' => 'Facebook', 'instagram' => 'Instagram', 'linkedin' => 'LinkedIn'] as $key => $label) {
        $wp_customize->add_setting("social_{$key}", ['sanitize_callback' => 'esc_url_raw', 'default' => '']);
        $wp_customize->add_control("social_{$key}", ['label' => "URL {$label}", 'section' => 'expertia360_social', 'type' => 'url']);
    }

    $wp_customize->add_section('expertia360_general', [
        'title'    => 'Texto del sitio',
        'priority' => 125,
    ]);
    $wp_customize->add_setting('about_text',      ['sanitize_callback' => 'wp_kses_post',      'default' => '']);
    $wp_customize->add_setting('footer_tagline',  ['sanitize_callback' => 'sanitize_text_field','default' => 'Revista digital independiente.']);
    $wp_customize->add_control('about_text',      ['label' => 'Texto "Sobre Expertia 360" (homepage)', 'section' => 'expertia360_general', 'type' => 'textarea']);
    $wp_customize->add_control('footer_tagline',  ['label' => 'Tagline del footer',                    'section' => 'expertia360_general', 'type' => 'text']);
}
add_action('customize_register', 'expertia360_customizer');

/* ----------------------------------------------------------
   LOAD MORE (AJAX)
   ---------------------------------------------------------- */
function expertia360_load_more() {
    check_ajax_referer('expertia360_nonce', 'nonce');

    $page     = max(1, absint($_POST['page'] ?? 1));
    $cat      = absint($_POST['cat']  ?? 0);
    $per_page = 6;

    $query = new WP_Query([
        'post_type'      => 'post',
        'posts_per_page' => $per_page,
        'paged'          => $page,
        'cat'            => $cat ?: null,
        'post_status'    => 'publish',
    ]);

    $html = '';
    if ($query->have_posts()) {
        while ($query->have_posts()) {
            $query->the_post();
            ob_start();
            get_template_part('template-parts/article-card');
            $html .= ob_get_clean();
        }
    }
    wp_reset_postdata();

    wp_send_json_success([
        'html'      => $html,
        'max_pages' => $query->max_num_pages,
    ]);
}
add_action('wp_ajax_expertia360_load_more',        'expertia360_load_more');
add_action('wp_ajax_nopriv_expertia360_load_more', 'expertia360_load_more');

/* ----------------------------------------------------------
   DISABLE EMOJIS (performance)
   ---------------------------------------------------------- */
remove_action('wp_head',             'print_emoji_detection_script', 7);
remove_action('wp_print_styles',     'print_emoji_styles');
remove_action('admin_print_scripts', 'print_emoji_detection_script');
remove_action('admin_print_styles',  'print_emoji_styles');
