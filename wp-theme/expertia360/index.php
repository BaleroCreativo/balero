<?php get_header(); ?>

<main id="main" class="site-main">
  <div class="container" style="padding:48px 24px;">

    <?php if (have_posts()) : ?>
      <h1 class="section-heading"><?php is_home() && !is_front_page() ? single_post_title() : the_archive_title(); ?></h1>
      <div class="grid-3" style="margin-top:32px;">
        <?php while (have_posts()) : the_post(); ?>
          <?php get_template_part('template-parts/article-card'); ?>
        <?php endwhile; ?>
      </div>
      <div class="posts-pagination"><?php the_posts_pagination(['prev_text' => '‹', 'next_text' => '›']); ?></div>
    <?php else : ?>
      <p>No se encontraron artículos.</p>
    <?php endif; ?>

  </div>
</main>

<?php get_footer(); ?>
