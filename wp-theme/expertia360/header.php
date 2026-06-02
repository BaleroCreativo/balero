<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
  <meta charset="<?php bloginfo('charset'); ?>">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="profile" href="https://gmpg.org/xfn/11">
  <?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<?php
// Determine layout: institutional pages use secondary nav, no subscribe button
$is_institutional = is_page(['nosotros', 'contacto', 'publica-con-nosotros', 'anunciate-o-publica', 'transparencia-legal', 'aviso-legal', 'privacidad', 'politica-de-cookies']);
?>

<div id="page" class="site">

  <!-- Top Bar -->
  <div class="top-bar<?php echo $is_institutional ? ' top-bar--minimal' : ''; ?>">
    <span class="top-bar__date">
      Actualizado: <?php echo esc_html(date_i18n('j \d\e F, Y')); ?>
    </span>
    <?php if (!$is_institutional) : ?>
      <a href="#newsletter" class="btn btn--dark" style="font-size:11px;padding:7px 16px;">Suscríbete</a>
    <?php endif; ?>
  </div>

  <!-- Site Header -->
  <header class="site-header" id="masthead">

    <?php // Logo ?>
    <a href="<?php echo esc_url(home_url('/')); ?>" class="site-logo" rel="home">
      <?php
      if (has_custom_logo()) {
          $logo_id  = get_theme_mod('custom_logo');
          $logo_img = wp_get_attachment_image($logo_id, 'full');
          echo $logo_img;
      } else {
          bloginfo('name');
      }
      ?>
    </a>

    <?php // Mobile toggle ?>
    <button class="nav-toggle" aria-controls="primary-menu" aria-expanded="false" aria-label="Menú">
      <span class="nav-toggle__bar"></span>
      <span class="nav-toggle__bar"></span>
      <span class="nav-toggle__bar"></span>
    </button>

    <?php if ($is_institutional) : ?>
      <nav class="nav-secondary" id="secondary-menu" aria-label="Menú institucional">
        <?php
        wp_nav_menu([
          'theme_location' => 'secondary',
          'menu_id'        => 'secondary-menu-list',
          'container'      => false,
          'menu_class'     => 'nav-list',
          'fallback_cb'    => function() {
              echo '<ul class="nav-list">
                <li class="nav-list__item"><a class="nav-list__link" href="' . esc_url(home_url('/nosotros/'))             . '">Nosotros</a></li>
                <li class="nav-list__item"><a class="nav-list__link" href="' . esc_url(home_url('/contacto/'))             . '">Contacto</a></li>
                <li class="nav-list__item"><a class="nav-list__link" href="' . esc_url(home_url('/publica-con-nosotros/')) . '">Publica con nosotros</a></li>
              </ul>';
          },
          'add_li_class'   => 'nav-list__item',
          'link_class'     => 'nav-list__link',
        ]);
        ?>
      </nav>
    <?php else : ?>
      <nav class="nav-primary" id="primary-menu" aria-label="Menú principal">
        <?php
        wp_nav_menu([
          'theme_location' => 'primary',
          'menu_id'        => 'primary-menu-list',
          'container'      => false,
          'menu_class'     => 'nav-list',
          'fallback_cb'    => function() {
              $cats = get_categories(['number' => 5, 'hide_empty' => false]);
              echo '<ul class="nav-list">';
              foreach ($cats as $cat) {
                  echo '<li class="nav-list__item"><a class="nav-list__link" href="' . esc_url(get_category_link($cat->term_id)) . '">' . esc_html($cat->name) . '</a></li>';
              }
              echo '</ul>';
          },
          'add_li_class'   => 'nav-list__item',
          'link_class'     => 'nav-list__link',
        ]);
        ?>
      </nav>
    <?php endif; ?>

  </header><!-- #masthead -->
