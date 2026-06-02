<?php
/*
 * Template Name: Transparencia Legal
 */
get_header();
?>

<main id="main" class="site-main">
  <div class="legal-page">

    <p class="legal-page__eyebrow">Categoría</p>

    <?php while (have_posts()) : the_post(); ?>
      <h1 class="legal-page__title"><?php the_title(); ?></h1>
      <p class="legal-page__subtitle"><?php the_excerpt(); ?></p>
      <div class="legal-page__content">
        <?php the_content(); ?>
      </div>
    <?php endwhile; ?>

  </div>
</main>

<?php get_footer(); ?>
