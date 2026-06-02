<?php
/*
 * Template Name: Nosotros
 */
get_header();
?>

<main id="main" class="site-main">

  <!-- Hero: Texto + Imagen -->
  <section class="about-hero">
    <div class="container grid-2">
      <div class="about-hero__text">
        <?php while (have_posts()) : the_post(); ?>
          <h1><?php the_title(); ?></h1>
          <div><?php the_content(); ?></div>
          <a href="<?php echo esc_url(home_url('/contacto/')); ?>" class="btn btn--outline">Contáctenos</a>
        <?php endwhile; ?>
      </div>
      <div>
        <?php if (has_post_thumbnail()) : ?>
          <?php the_post_thumbnail('expertia-card', ['class' => 'about-hero__image']); ?>
        <?php else : ?>
          <div class="about-hero__image-placeholder">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48" style="opacity:.3">
              <path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/>
            </svg>
          </div>
        <?php endif; ?>
      </div>
    </div>
  </section>

  <!-- Nuestra Misión -->
  <section class="about-mission">
    <h2 class="about-mission__title">Nuestra misión</h2>
    <p class="about-mission__text">
      <?php echo wp_kses_post(get_post_meta(get_the_ID(), '_mission_text', true) ?: 'En Expertia 360 creemos en el periodismo independiente, riguroso y accesible. Nuestra misión es llevar contenido especializado a lectores exigentes que buscan profundidad y contexto en cada tema.'); ?>
    </p>
    <!-- Logo / Imagen de misión -->
    <div class="about-mission__logo-wrap">
      <?php
      $mission_img_id = get_post_meta(get_the_ID(), '_mission_image', true);
      if ($mission_img_id) {
          echo wp_get_attachment_image($mission_img_id, 'full', false, ['style' => 'width:100%;height:100%;object-fit:cover;border-radius:50%;']);
      } else {
          echo '<span style="font-family:var(--font-logo);font-size:48px;color:var(--gray-300);">' . get_bloginfo('name') . '</span>';
      }
      ?>
    </div>
  </section>

  <!-- CTA: ¿Quieres colaborar? -->
  <section class="about-cta">
    <div class="container">
      <h2 class="about-cta__title">¿Quieres colaborar con nosotros?</h2>
      <p class="about-cta__text">Si eres experto en tu área y quieres compartir tu conocimiento con nuestra comunidad, nos encantaría escucharte.</p>
      <a href="<?php echo esc_url(home_url('/publica-con-nosotros/')); ?>" class="btn btn--dark">Publica con nosotros</a>
    </div>
  </section>

</main>

<?php get_footer(); ?>
