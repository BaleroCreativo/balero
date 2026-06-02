<?php get_header(); ?>

<main id="main" class="site-main">
  <div class="container" style="padding:48px 24px;">
    <h1 class="section-heading">
      Resultados para: <em style="font-weight:400;"><?php echo get_search_query(); ?></em>
    </h1>

    <?php if (have_posts()) : ?>
      <p style="color:var(--gray-700);margin-bottom:28px;"><?php printf('%d resultado%s encontrado%s', $wp_query->found_posts, $wp_query->found_posts === 1 ? '' : 's', $wp_query->found_posts === 1 ? '' : 's'); ?></p>
      <div class="grid-3">
        <?php while (have_posts()) : the_post(); ?>
          <?php get_template_part('template-parts/article-card'); ?>
        <?php endwhile; ?>
      </div>
      <div class="posts-pagination"><?php the_posts_pagination(['prev_text' => '‹', 'next_text' => '›']); ?></div>
    <?php else : ?>
      <p style="color:var(--gray-700);">No se encontraron resultados para tu búsqueda. Intenta con otros términos.</p>
    <?php endif; ?>
  </div>
</main>

<?php get_footer(); ?>
