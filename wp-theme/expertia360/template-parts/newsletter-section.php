<section class="section-newsletter" id="newsletter">
  <div class="newsletter-inner">
    <h2 class="section-heading">Suscríbete</h2>
    <p>Recibe nuestros mejores artículos directamente en tu correo. Sin spam, solo contenido que importa.</p>

    <?php
    $nl_status = $_GET['nl'] ?? '';
    if ($nl_status === 'ok') :
    ?>
      <div class="form-message form-message--success">¡Gracias! Te has suscrito correctamente.</div>
    <?php elseif (in_array($nl_status, ['error','invalid'], true)) : ?>
      <div class="form-message form-message--error">Hubo un problema. Verifica tu correo e intenta de nuevo.</div>
    <?php endif; ?>

    <form class="newsletter-form" method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>">
      <input type="hidden" name="action" value="expertia360_newsletter">
      <?php wp_nonce_field('expertia360_newsletter'); ?>
      <input
        type="email"
        name="newsletter_email"
        class="newsletter-form__input"
        placeholder="Correo electrónico"
        required
        aria-label="Tu correo electrónico"
      >
      <button type="submit" class="newsletter-form__btn">Enviar</button>
    </form>
  </div>
</section>
