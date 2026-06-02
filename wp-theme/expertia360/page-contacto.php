<?php
/*
 * Template Name: Contacto
 */
get_header();
$cf_status = $_GET['cf'] ?? '';
?>

<main id="main" class="site-main">
  <div class="container">

    <!-- Page Header -->
    <div class="contact-page-header">
      <?php while (have_posts()) : the_post(); ?>
        <h1><?php the_title(); ?></h1>
        <p class="lead"><?php the_excerpt(); ?></p>
      <?php endwhile; ?>
    </div>

    <!-- Contact Body: Info + Form -->
    <div class="contact-body">

      <!-- Info -->
      <div class="contact-info">
        <?php
        $phone   = get_theme_mod('contact_phone',   '+52 (555) 000-0000');
        $email   = get_theme_mod('contact_email',   'contacto@expertia360.com');
        $address = get_theme_mod('contact_address', '');
        ?>

        <?php if ($phone) : ?>
          <div class="contact-info__item">
            <span class="contact-info__label">Teléfono</span>
            <p class="contact-info__value"><a href="tel:<?php echo esc_attr(preg_replace('/[^+\d]/', '', $phone)); ?>"><?php echo esc_html($phone); ?></a></p>
          </div>
        <?php endif; ?>

        <?php if ($email) : ?>
          <div class="contact-info__item">
            <span class="contact-info__label">Correo electrónico</span>
            <p class="contact-info__value"><a href="mailto:<?php echo esc_attr($email); ?>"><?php echo esc_html($email); ?></a></p>
          </div>
        <?php endif; ?>

        <?php if ($address) : ?>
          <div class="contact-info__item">
            <span class="contact-info__label">Dirección</span>
            <p class="contact-info__value"><?php echo nl2br(esc_html($address)); ?></p>
          </div>
        <?php endif; ?>
      </div>

      <!-- Form -->
      <div class="contact-form">
        <?php if ($cf_status === 'ok') : ?>
          <div class="form-message form-message--success" style="margin-bottom:24px;">¡Mensaje enviado! Te responderemos pronto.</div>
        <?php elseif (in_array($cf_status, ['error','invalid'], true)) : ?>
          <div class="form-message form-message--error" style="margin-bottom:24px;">Hubo un error. Verifica los campos e intenta de nuevo.</div>
        <?php endif; ?>

        <form method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>">
          <input type="hidden" name="action" value="expertia360_contact">
          <?php wp_nonce_field('expertia360_contact'); ?>

          <div class="form-group">
            <label class="form-label" for="contact_name">Nombre</label>
            <input class="form-input" type="text" id="contact_name" name="contact_name" placeholder="Tu nombre" required>
          </div>

          <div class="form-group">
            <label class="form-label" for="contact_email">E-mail</label>
            <input class="form-input" type="email" id="contact_email" name="contact_email" placeholder="Tu e-mail" required>
          </div>

          <div class="form-group">
            <label class="form-label" for="contact_phone">Teléfono</label>
            <div class="phone-group">
              <span class="phone-prefix">MX +52</span>
              <input class="form-input" type="tel" id="contact_phone" name="contact_phone" placeholder="(555) 000-0000">
            </div>
          </div>

          <div class="form-group">
            <label class="form-label" for="contact_message">Mensaje</label>
            <textarea class="form-textarea" id="contact_message" name="contact_message" placeholder="¿En qué podemos ayudarte?" required></textarea>
          </div>

          <p class="form-privacy">
            Al enviar este formulario aceptas la <a href="<?php echo esc_url(home_url('/privacidad/')); ?>">Política de Privacidad</a>.
          </p>

          <button type="submit" class="btn btn--dark btn--full">Enviar</button>
        </form>
      </div>

    </div><!-- .contact-body -->

    <!-- Map placeholder -->
    <?php $map_embed = get_theme_mod('contact_map_embed', ''); ?>
    <?php if ($map_embed) : ?>
      <div class="contact-map-placeholder" style="height:auto;background:none;display:block;">
        <?php echo $map_embed; // Must be an embed iframe — set via Customizer ?>
      </div>
    <?php else : ?>
      <div class="contact-map-placeholder">
        <span>Mapa — configura la ubicación en el Personalizador</span>
      </div>
    <?php endif; ?>

  </div><!-- .container -->
</main>

<?php get_footer(); ?>
