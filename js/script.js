/**
 * Suraj Dattatray Ghadage Portfolio Website
 * Pure Vanilla JavaScript — Zero External Runtime Dependencies
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initMobileMenu();
  initScrollSpy();
  initScrollReveal();
  initBackToTop();
  initContactForm();
});

/* --- 1. Sticky Navbar Elevation --- */
function initNavbar() {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;

  const handleScroll = () => {
    if (window.scrollY > 30) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

/* --- 2. Mobile Menu Toggle --- */
function initMobileMenu() {
  const toggleBtn = document.getElementById('mobileMenuBtn');
  const menu = document.getElementById('mobileMenu');
  const menuIcon = document.getElementById('menuIcon');
  if (!toggleBtn || !menu) return;

  const toggle = () => {
    const isHidden = menu.classList.contains('hidden');
    if (isHidden) {
      menu.classList.remove('hidden');
      toggleBtn.setAttribute('aria-expanded', 'true');
      if (menuIcon) {
        menuIcon.classList.remove('fa-bars');
        menuIcon.classList.add('fa-xmark');
      }
    } else {
      menu.classList.add('hidden');
      toggleBtn.setAttribute('aria-expanded', 'false');
      if (menuIcon) {
        menuIcon.classList.remove('fa-xmark');
        menuIcon.classList.add('fa-bars');
      }
    }
  };

  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    toggle();
  });

  // Close menu when clicking on any mobile nav link
  const links = menu.querySelectorAll('a');
  links.forEach(link => {
    link.addEventListener('click', () => {
      menu.classList.add('hidden');
      toggleBtn.setAttribute('aria-expanded', 'false');
      if (menuIcon) {
        menuIcon.classList.remove('fa-xmark');
        menuIcon.classList.add('fa-bars');
      }
    });
  });

  // Close menu when clicking outside
  document.addEventListener('click', (e) => {
    if (!menu.contains(e.target) && !toggleBtn.contains(e.target)) {
      menu.classList.add('hidden');
      toggleBtn.setAttribute('aria-expanded', 'false');
      if (menuIcon) {
        menuIcon.classList.remove('fa-xmark');
        menuIcon.classList.add('fa-bars');
      }
    }
  });
}

/* --- 3. Scroll Spy & Active Nav Highlighting --- */
function initScrollSpy() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.desktop-nav .nav-link, .mobile-nav-link');
  if (!sections.length || !navLinks.length) return;

  const observerOptions = {
    root: null,
    rootMargin: '-20% 0px -70% 0px',
    threshold: 0
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          const href = link.getAttribute('href');
          if (href === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(sec => observer.observe(sec));
}

/* --- 4. IntersectionObserver Scroll Reveal Animations --- */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal-fade');
  if (!revealElements.length) return;

  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target); // Trigger once per brief requirements
        }
      });
    }, {
      root: null,
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => revealObserver.observe(el));
  } else {
    // Fallback if IntersectionObserver not supported
    revealElements.forEach(el => el.classList.add('active'));
  }
}

/* --- 5. Back to Top Floating Button --- */
function initBackToTop() {
  const backToTopBtn = document.getElementById('backToTop');
  if (!backToTopBtn) return;

  const toggleBtnVisibility = () => {
    if (window.scrollY > 400) {
      backToTopBtn.classList.remove('hidden');
    } else {
      backToTopBtn.classList.add('hidden');
    }
  };

  window.addEventListener('scroll', toggleBtnVisibility, { passive: true });
  toggleBtnVisibility();

  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

/* --- 6. Clipboard Copy Utility & Toast Notification --- */
function copyToClipboard(text, successMessage = 'Copied to clipboard!') {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(() => {
      showToast(successMessage);
    }).catch(() => {
      fallbackCopy(text, successMessage);
    });
  } else {
    fallbackCopy(text, successMessage);
  }
}

function fallbackCopy(text, successMessage) {
  const tempInput = document.createElement('input');
  tempInput.value = text;
  document.body.appendChild(tempInput);
  tempInput.select();
  try {
    document.execCommand('copy');
    showToast(successMessage);
  } catch (err) {
    showToast('Failed to copy. Please copy manually: ' + text);
  }
  document.body.removeChild(tempInput);
}

function showToast(message) {
  const toast = document.getElementById('toast');
  if (!toast) return;

  toast.innerHTML = `<i class="fa-solid fa-circle-check text-accent-cyan"></i> <span>${message}</span>`;
  toast.classList.remove('hidden');

  clearTimeout(window.toastTimer);
  window.toastTimer = setTimeout(() => {
    toast.classList.add('hidden');
  }, 3200);
}

// Make copyToClipboard globally accessible for inline onclick handlers
window.copyToClipboard = copyToClipboard;

/* --- 7. Contact Form Handler (Formspree AJAX + Fallback) --- */
function initContactForm() {
  const form = document.getElementById('contactForm');
  if (!form) return;

  const submitBtn = document.getElementById('submitBtn');
  const btnText = document.getElementById('btnText');
  const btnIcon = document.getElementById('btnIcon');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = form.name.value.trim();
    const email = form.email.value.trim();
    const subject = form.subject ? form.subject.value.trim() : 'Portfolio Inquiry';
    const message = form.message.value.trim();

    if (!name || !email || !message) {
      showToast('Please fill out all required fields.');
      return;
    }

    // Set loading state
    if (submitBtn) submitBtn.disabled = true;
    if (btnText) btnText.textContent = 'Sending...';
    if (btnIcon) btnIcon.className = 'fa-solid fa-spinner fa-spin';

    try {
      const response = await fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: {
          'Accept': 'application/json'
        }
      });

      if (response.ok) {
        showToast('Thank you! Your message has been sent successfully.');
        form.reset();
      } else {
        // Formspree not yet verified or error -> provide direct mailto fallback
        showToast('Message sent! Opening fallback email draft...');
        window.location.href = `mailto:surajghadage1206@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent("From: " + name + " (" + email + ")\n\n" + message)}`;
      }
    } catch (error) {
      // Network failure -> mailto fallback
      showToast('Redirecting to default email client...');
      window.location.href = `mailto:surajghadage1206@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent("From: " + name + " (" + email + ")\n\n" + message)}`;
    } finally {
      if (submitBtn) submitBtn.disabled = false;
      if (btnText) btnText.textContent = 'Send Message';
      if (btnIcon) btnIcon.className = 'fa-regular fa-paper-plane';
    }
  });
}
