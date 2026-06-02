<?php get_header(); ?>

<main id="main" class="site-main">

  <!-- Archive Header -->
  <div class="archive-header">
    <?php if (is_category()) : ?>
      <p class="archive-header__category">Temática</p>
      <h1 class="archive-header__title"><?php single_cat_title(); ?></h1>
      <?php
      $total = $wp_query->found_posts;
      echo '<p class="archive-header__count">' . sprintf('%d artículo%s publicado%s', $total, $total === 1 ? '' : 's', $total === 1 ? '' : 's') . '</p>';
      ?>
    <?php elseif (is_tag()) : ?>
      <h1 class="archive-header__title"><?php single_tag_title(); ?></h1>
    <?php elseif (is_author()) : ?>
      <p class="archive-header__category">Autor</p>
      <h1 class="archive-header__title"><?php the_author_meta('display_name', get_queried_object_id()); ?></h1>
    <?php else : ?>
      <h1 class="archive-header__title"><?php the_archive_title(); ?></h1>
    <?php endif; ?>
  </div>

  <?php if (have_posts()) : ?>

    <!-- Featured first post -->
    <?php the_post(); $featured_id = get_the_ID(); $fcats = get_the_category(); ?>
    <div class="archive-featured">
      <div class="container">
        <a href="<?php the_permalink(); ?>">
          <?php if (has_post_thumbnail()) : ?>
            <?php the_post_thumbnail('expertia-featured', ['class' => 'archive-featured__image', 'loading' => 'eager']); ?>
          <?php else : ?>
            <div class="archive-featured__image-placeholder">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="60" height="60" style="opacity:.3">
                <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
              </svg>
            </div>
          <?php endif; ?>
        </a>
        <?php if ($fcats) : ?>
          <p class="archive-featured__category"><?php echo esc_html($fcats[0]->name); ?></p>
        <?php endif; ?>
        <h2 class="archive-featured__title">
          <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
        </h2>
        <p class="archive-featured__excerpt"><?php echo wp_trim_words(get_the_excerpt(), 30, '…'); ?></p>
        <div class="archive-featured__meta">
          <span>POR <?php the_author(); ?></span>
          <span><?php echo expertia360_reading_time(); ?></span>
        </div>
      </div>
    </div>

    <!-- Grid of remaining posts -->
    <?php if (have_posts()) : ?>
      <div class="archive-grid">
        <div class="container">
          <div class="grid-3" id="posts-grid">
            <?php while (have_posts()) : the_post(); ?>
              <?php get_template_part('template-parts/article-card'); ?>
            <?php endwhile; ?>
          </div>

          <!-- Load more / Pagination -->
          <?php
          $max_pages   = $wp_query->max_num_pages;
          $current_cat = is_category() ? get_queried_object_id() : 0;
          ?>
          <?php if ($max_pages > 1) : ?>
            <div class="load-more-wrap">
              <button
                class="btn btn--dark"
                id="load-more-btn"
                data-page="2"
                data-max="<?php echo esc_attr($max_pages); ?>"
                data-cat="<?php echo esc_attr($current_cat); ?>"
              >
                Ver más
              </button>
            </div>
          <?php endif; ?>

        </div>
      </div>
    <?php endif; ?>

  <?php else : ?>

    <div class="container" style="padding:60px 24px;text-align:center;">
      <p>No hay artículos en esta sección todavía.</p>
    </div>

  <?php endif; ?>

  <?php get_template_part('template-parts/newsletter-section'); ?>

</main>

<?php get_footer(); ?>
