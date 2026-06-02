<?php
/*
 * Template Name: Publica con nosotros
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

    <!-- Contact: Info email + Form -->
    <div class="contact-body">
      <div class="contact-info">
        <?php $email = get_theme_mod('contact_email', 'contacto@expertia360.com'); ?>
        <p style="font-size:14px;color:var(--gray-700);margin-bottom:12px;">También puedes enviarnos un correo a:</p>
        <p class="contact-info__value"><a href="mailto:<?php echo esc_attr($email); ?>"><?php echo esc_html($email); ?></a></p>
      </div>

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
            <label class="form-label" for="pub_name">Nombre</label>
            <input class="form-input" type="text" id="pub_name" name="contact_name" placeholder="Tu nombre" required>
          </div>

          <div class="form-group">
            <label class="form-label" for="pub_email">E-mail</label>
            <input class="form-input" type="email" id="pub_email" name="contact_email" placeholder="Tu e-mail" required>
          </div>

          <div class="form-group">
            <label class="form-label" for="pub_phone">Teléfono</label>
            <div class="phone-group">
              <span class="phone-prefix">MX +52</span>
              <input class="form-input" type="tel" id="pub_phone" name="contact_phone" placeholder="(555) 000-0000">
            </div>
          </div>

          <div class="form-group">
            <label class="form-label" for="pub_message">Mensaje</label>
            <textarea class="form-textarea" id="pub_message" name="contact_message"
              placeholder="Indica si te gustaría anunciarte en la revista o publicar algún artículo." required></textarea>
          </div>

          <p class="form-privacy">
            Al enviar este formulario aceptas la <a href="<?php echo esc_url(home_url('/privacidad/')); ?>">Política de Privacidad</a>.
          </p>

          <button type="submit" class="btn btn--dark btn--full">Enviar</button>
        </form>
      </div>
    </div>

    <!-- Benefits Section -->
    <div class="benefits-section">
      <div class="benefits-cta">
        <h2 class="benefits-cta__title">Publica con nosotros y llega donde importa.</h2>
        <p class="benefits-cta__text">Nuestra revista digital conecta tu marca con lectores especializados. Ya sea un artículo editorial o una campaña publicitaria, aquí tu presencia genera impacto real.</p>
        <a href="#" class="btn btn--outline" onclick="document.getElementById('pub_name').focus();return false;">Solicitar información</a>
      </div>

      <div class="benefits-list">
        <?php
        $benefits = [
          ['icon' => '📊', 'title' => 'Audiencia especializada',     'text' => 'Llegamos a lectores con intereses específicos y alto poder adquisitivo en múltiples industrias.'],
          ['icon' => '✍️', 'title' => 'Contenido editorial',         'text' => 'Publicamos artículos de opinión, análisis y tendencias escritos por expertos en su área.'],
          ['icon' => '📱', 'title' => 'Presencia digital completa',  'text' => 'Tu marca aparece en nuestra revista web y en nuestros canales de distribución en redes sociales.'],
          ['icon' => '📈', 'title' => 'Métricas transparentes',      'text' => 'Te proporcionamos estadísticas detalladas sobre el alcance y desempeño de tu contenido.'],
          ['icon' => '🤝', 'title' => 'Alianzas a largo plazo',      'text' => 'Construimos relaciones duraderas con anunciantes y colaboradores que comparten nuestra visión editorial.'],
        ];
        foreach ($benefits as $b) :
        ?>
          <div class="benefit-item">
            <div class="benefit-item__icon"><?php echo $b['icon']; ?></div>
            <div class="benefit-item__content">
              <p class="benefit-item__title"><?php echo esc_html($b['title']); ?></p>
              <p class="benefit-item__text"><?php echo esc_html($b['text']); ?></p>
            </div>
          </div>
        <?php endforeach; ?>
      </div>
    </div>

  </div><!-- .container -->
</main>

<?php get_footer(); ?>
