  <footer class="site-footer" id="colophon">
    <div class="footer-main">

      <!-- Brand -->
      <div class="footer-brand">
        <a href="<?php echo esc_url(home_url('/')); ?>" class="footer-logo">
          <?php bloginfo('name'); ?>
        </a>
        <p class="footer-tagline"><?php echo esc_html(get_theme_mod('footer_tagline', 'Revista digital independiente.')); ?></p>
      </div>

      <!-- Secciones -->
      <div class="footer-nav">
        <p class="footer-nav__heading">Secciones</p>
        <?php
        wp_nav_menu([
          'theme_location' => 'footer-secciones',
          'container'      => false,
          'menu_class'     => 'footer-nav__list',
          'fallback_cb'    => function() {
              $cats = get_categories(['number' => 5, 'hide_empty' => false]);
              echo '<ul class="footer-nav__list">';
              foreach ($cats as $cat) {
                  echo '<li><a href="' . esc_url(get_category_link($cat->term_id)) . '">' . esc_html($cat->name) . '</a></li>';
              }
              echo '</ul>';
          },
        ]);
        ?>
      </div>

      <!-- Revista -->
      <div class="footer-nav">
        <p class="footer-nav__heading">Revista</p>
        <?php
        wp_nav_menu([
          'theme_location' => 'footer-revista',
          'container'      => false,
          'menu_class'     => 'footer-nav__list',
          'fallback_cb'    => function() {
              echo '<ul class="footer-nav__list">
                <li><a href="' . esc_url(home_url('/nosotros/'))             . '">Sobre nosotros</a></li>
                <li><a href="' . esc_url(home_url('/publica-con-nosotros/')) . '">Publica tu artículo</a></li>
                <li><a href="' . esc_url(home_url('/contacto/'))             . '">Contacto</a></li>
              </ul>';
          },
        ]);
        ?>
      </div>

      <!-- Legal -->
      <div class="footer-nav">
        <p class="footer-nav__heading">Legal</p>
        <?php
        wp_nav_menu([
          'theme_location' => 'footer-legal',
          'container'      => false,
          'menu_class'     => 'footer-nav__list',
          'fallback_cb'    => function() {
              echo '<ul class="footer-nav__list">
                <li><a href="' . esc_url(home_url('/aviso-legal/'))          . '">Aviso legal</a></li>
                <li><a href="' . esc_url(home_url('/privacidad/'))           . '">Privacidad</a></li>
                <li><a href="' . esc_url(home_url('/politica-de-cookies/'))  . '">Política de cookies</a></li>
              </ul>';
          },
        ]);
        ?>
      </div>

    </div><!-- .footer-main -->

    <div class="footer-bottom">
      <p class="footer-copyright">
        &copy; <?php echo date('Y'); ?> <?php bloginfo('name'); ?>. Todos los derechos reservados.
      </p>
      <?php expertia360_social_links(); ?>
    </div>

  </footer><!-- #colophon -->

</div><!-- #page -->

<?php wp_footer(); ?>
</body>
</html>
