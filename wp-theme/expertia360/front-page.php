<?php get_header(); ?>

<main id="main" class="site-main">

  <!-- =====================================================
       HERO: Featured + Sidebar "Más recientes"
       ===================================================== -->
  <?php
  $featured_query = new WP_Query([
    'posts_per_page' => 1,
    'post_status'    => 'publish',
    'meta_key'       => '_expertia_featured',
    'meta_value'     => '1',
    'ignore_sticky_posts' => true,
  ]);

  // Fallback: latest sticky, or simply latest post
  if (!$featured_query->have_posts()) {
      $sticky = get_option('sticky_posts');
      $featured_query = new WP_Query([
        'posts_per_page'      => 1,
        'post_status'         => 'publish',
        'post__in'            => $sticky ?: [0],
        'ignore_sticky_posts' => false,
      ]);
  }
  if (!$featured_query->have_posts()) {
      $featured_query = new WP_Query(['posts_per_page' => 1, 'post_status' => 'publish']);
  }
  $featured_id = 0;
  ?>

  <div class="home-hero container">

    <!-- Featured article -->
    <?php if ($featured_query->have_posts()) : $featured_query->the_post(); $featured_id = get_the_ID(); ?>
      <article class="hero-featured">

        <a href="<?php the_permalink(); ?>">
          <?php if (has_post_thumbnail()) : ?>
            <?php the_post_thumbnail('expertia-hero', ['class' => 'hero-featured__image', 'loading' => 'eager']); ?>
          <?php else : ?>
            <div class="hero-featured__image-placeholder">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="60" height="60" style="opacity:.3">
                <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
              </svg>
            </div>
          <?php endif; ?>
        </a>

        <?php $cats = get_the_category(); if ($cats) : ?>
          <a href="<?php echo esc_url(get_category_link($cats[0]->term_id)); ?>" class="hero-featured__category">
            <?php echo esc_html($cats[0]->name); ?>
          </a>
        <?php endif; ?>

        <h1 class="hero-featured__title">
          <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
        </h1>

        <p class="hero-featured__excerpt"><?php echo wp_trim_words(get_the_excerpt(), 35, '…'); ?></p>

        <div class="hero-featured__meta">
          <span>POR <?php the_author(); ?></span>
          <span><?php echo expertia360_reading_time(); ?></span>
        </div>

      </article>
    <?php endif; wp_reset_postdata(); ?>

    <!-- Sidebar: Más recientes -->
    <aside class="hero-sidebar">
      <p class="hero-sidebar__title">Más recientes</p>

      <?php
      $recent_query = new WP_Query([
        'posts_per_page'      => 4,
        'post_status'         => 'publish',
        'post__not_in'        => $featured_id ? [$featured_id] : [],
        'ignore_sticky_posts' => true,
      ]);
      ?>

      <?php if ($recent_query->have_posts()) : ?>
        <div class="recent-list">
          <?php while ($recent_query->have_posts()) : $recent_query->the_post();
            $rcats = get_the_category();
          ?>
            <div class="recent-item">
              <?php if ($rcats) : ?>
                <a href="<?php echo esc_url(get_category_link($rcats[0]->term_id)); ?>" class="recent-item__category">
                  <?php echo esc_html($rcats[0]->name); ?>
                </a>
              <?php endif; ?>
              <h3 class="recent-item__title">
                <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
              </h3>
              <p class="recent-item__excerpt"><?php echo wp_trim_words(get_the_excerpt(), 15, '…'); ?></p>
              <div class="recent-item__meta">
                <span>POR <?php the_author(); ?></span>
                <span><?php echo expertia360_reading_time(); ?></span>
              </div>
            </div>
          <?php endwhile; wp_reset_postdata(); ?>
        </div>
      <?php endif; ?>
    </aside>

  </div><!-- .home-hero -->

  <!-- =====================================================
       DESTACADOS
       ===================================================== -->
  <section class="section-destacados">
    <div class="container">
      <h2 class="section-heading">Destacados</h2>

      <?php
      $destacados = new WP_Query([
        'posts_per_page'      => 6,
        'post_status'         => 'publish',
        'post__not_in'        => $featured_id ? [$featured_id] : [],
        'ignore_sticky_posts' => true,
      ]);
      ?>

      <?php if ($destacados->have_posts()) : ?>
        <div class="grid-3">
          <?php while ($destacados->have_posts()) : $destacados->the_post(); ?>
            <?php get_template_part('template-parts/article-card'); ?>
          <?php endwhile; wp_reset_postdata(); ?>
        </div>
      <?php endif; ?>
    </div>
  </section>

  <!-- =====================================================
       SOBRE EXPERTIA 360
       ===================================================== -->
  <?php
  $about_text = get_theme_mod('about_text', '');
  if (!$about_text) {
      $about_text = get_bloginfo('description');
  }
  if ($about_text) :
  ?>
  <section class="section-about">
    <h2 class="section-about__title">Sobre <?php bloginfo('name'); ?></h2>
    <div class="section-about__text"><?php echo wp_kses_post($about_text); ?></div>
  </section>
  <?php endif; ?>

  <!-- Newsletter -->
  <?php get_template_part('template-parts/newsletter-section'); ?>

</main>

<?php get_footer(); ?>
