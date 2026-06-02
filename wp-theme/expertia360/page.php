<?php get_header(); ?>

<main id="main" class="site-main">
  <div class="legal-page">
    <?php while (have_posts()) : the_post(); ?>
      <h1 class="legal-page__title"><?php the_title(); ?></h1>
      <div class="legal-page__content">
        <?php the_content(); ?>
      </div>
    <?php endwhile; ?>
  </div>
</main>

<?php get_footer(); ?>
