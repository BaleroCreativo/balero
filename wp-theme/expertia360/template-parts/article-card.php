<article id="post-<?php the_ID(); ?>" <?php post_class('article-card'); ?>>

  <!-- Image -->
  <a href="<?php the_permalink(); ?>" class="article-card__image-link" tabindex="-1" aria-hidden="true">
    <div class="article-card__image-wrap">
      <?php if (has_post_thumbnail()) : ?>
        <?php the_post_thumbnail('expertia-card', ['loading' => 'lazy']); ?>
      <?php else : ?>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="40" height="40" style="opacity:.3">
          <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
        </svg>
      <?php endif; ?>
    </div>
  </a>

  <!-- Body -->
  <div class="article-card__body">
    <?php
    $cats = get_the_category();
    if ($cats) :
      $cat = $cats[0];
    ?>
      <a href="<?php echo esc_url(get_category_link($cat->term_id)); ?>" class="article-card__category">
        <?php echo esc_html($cat->name); ?>
      </a>
    <?php endif; ?>

    <h3 class="article-card__title">
      <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
    </h3>

    <p class="article-card__excerpt"><?php echo wp_trim_words(get_the_excerpt(), 20, '…'); ?></p>

    <div class="article-card__meta">
      <span>POR <?php the_author(); ?></span>
      <span><?php echo expertia360_reading_time(); ?></span>
    </div>
  </div>

</article>
