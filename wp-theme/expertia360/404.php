<?php get_header(); ?>

<main id="main" class="site-main">
  <div class="container" style="padding:80px 24px;text-align:center;">
    <p style="font-size:80px;font-weight:800;color:var(--gray-200);line-height:1;margin-bottom:16px;">404</p>
    <h1 style="font-size:28px;margin-bottom:12px;">Página no encontrada</h1>
    <p style="color:var(--gray-700);margin-bottom:28px;">El artículo que buscas ya no está aquí o fue movido.</p>
    <a href="<?php echo esc_url(home_url('/')); ?>" class="btn btn--dark">Volver al inicio</a>
  </div>
</main>

<?php get_footer(); ?>
