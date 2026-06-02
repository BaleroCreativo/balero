<?php get_header(); ?>

<main id="main" class="site-main">
  <?php while (have_posts()) : the_post(); ?>

    <!-- Post Header -->
    <div class="single-header">
      <div class="single-header__container">

        <?php $cats = get_the_category(); if ($cats) : ?>
          <a href="<?php echo esc_url(get_category_link($cats[0]->term_id)); ?>" class="single-header__category">
            <?php echo esc_html($cats[0]->name); ?>
          </a>
        <?php endif; ?>

        <h1 class="single-header__title"><?php the_title(); ?></h1>

        <div class="single-header__meta">
          <span class="author">POR <?php the_author(); ?></span>
          <span class="separator">·</span>
          <span class="date"><?php echo get_the_date('j \d\e F, Y'); ?></span>
          <span class="separator">·</span>
          <span class="reading-time"><?php echo expertia360_reading_time(); ?> de lectura</span>
        </div>

      </div>
    </div>

    <!-- Featured Image -->
    <?php if (has_post_thumbnail()) : ?>
      <?php the_post_thumbnail('expertia-hero', ['class' => 'single-featured-image', 'loading' => 'eager']); ?>
    <?php else : ?>
      <div class="single-featured-image-placeholder">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="64" height="64" style="opacity:.3">
          <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
        </svg>
      </div>
    <?php endif; ?>

    <!-- Post Content -->
    <div class="post-content">
      <?php the_content(); ?>
    </div>

    <!-- Author Bio -->
    <div class="author-bio">
      <p class="author-bio__heading">Sobre el autor</p>
      <p class="author-bio__name"><?php the_author(); ?></p>
      <?php $bio = get_the_author_meta('description'); if ($bio) : ?>
        <p class="author-bio__description"><?php echo esc_html($bio); ?></p>
      <?php endif; ?>
    </div>

  <?php endwhile; ?>

  <!-- Continue Reading -->
  <?php
  $cats = get_the_category(get_the_ID());
  $cat_ids = $cats ? wp_list_pluck($cats, 'term_id') : [];
  $related = new WP_Query([
    'posts_per_page'      => 3,
    'post_status'         => 'publish',
    'post__not_in'        => [get_the_ID()],
    'category__in'        => $cat_ids,
    'ignore_sticky_posts' => true,
    'orderby'             => 'rand',
  ]);
  if (!$related->have_posts()) {
      $related = new WP_Query(['posts_per_page' => 3, 'post_status' => 'publish', 'post__not_in' => [get_the_ID()]]);
  }
  ?>

  <?php if ($related->have_posts()) : ?>
    <section class="continue-reading">
      <div class="container">
        <h2 class="section-heading">Continúa leyendo</h2>
        <div class="grid-3">
          <?php while ($related->have_posts()) : $related->the_post(); ?>
            <?php get_template_part('template-parts/article-card'); ?>
          <?php endwhile; wp_reset_postdata(); ?>
        </div>
      </div>
    </section>
  <?php endif; ?>

  <?php get_template_part('template-parts/newsletter-section'); ?>

</main>

<?php get_footer(); ?>
