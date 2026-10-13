const motivationCard = document.querySelector("[data-motivation-card]");
const openMotivation = document.querySelector("[data-open-motivation]");
const closeMotivation = document.querySelector("[data-close-motivation]");
const track = document.querySelector("[data-carousel-track]");
const prev = document.querySelector("[data-carousel-prev]");
const next = document.querySelector("[data-carousel-next]");
const sendSuggestion = document.querySelector("[data-send-suggestion]");
const suggestionPopup = document.querySelector("[data-suggestion-popup]");
const closeSuggestion = document.querySelector("[data-close-suggestion]");
const popupMessage = document.querySelector("[data-popup-message]");
const suggestionInput = document.querySelector("[name='book']");
const downloadButtons = document.querySelectorAll(".book-actions button");
let suggestionTimer;

if (motivationCard && openMotivation && closeMotivation) {
  openMotivation.addEventListener("click", () => {
    motivationCard.hidden = false;
    motivationCard.scrollIntoView({ behavior: "smooth", block: "center" });
  });

  closeMotivation.addEventListener("click", () => {
    motivationCard.hidden = true;
  });
}

if (track && prev && next) {
  const cards = Array.from(track.children);
  let index = 0;
  let maxIndex = 0;

  const getCarouselMetrics = () => {
    const card = cards[0];
    const gap = Number.parseFloat(getComputedStyle(track).gap) || 0;
    const cardWidth = card.getBoundingClientRect().width + gap;
    const windowWidth = track.parentElement.getBoundingClientRect().width;
    const visibleCards = Math.max(1, Math.floor((windowWidth + gap) / cardWidth));

    return {
      cardWidth,
      visibleCards,
      maxIndex: Math.max(0, cards.length - visibleCards),
    };
  };

  const updateCarousel = () => {
    const metrics = getCarouselMetrics();
    maxIndex = metrics.maxIndex;
    index = Math.min(index, maxIndex);
    track.style.transform = `translateX(${-index * metrics.cardWidth}px)`;
  };

  const go = (direction) => {
    const metrics = getCarouselMetrics();
    maxIndex = metrics.maxIndex;

    if (direction > 0 && index >= maxIndex) {
      index = 0;
    } else if (direction < 0 && index <= 0) {
      index = maxIndex;
    } else {
      index += direction;
    }

    updateCarousel();
  };

  next.addEventListener("click", () => go(1));
  prev.addEventListener("click", () => go(-1));
  window.addEventListener("resize", updateCarousel);
  window.setInterval(() => go(1), 5200);
}

if (suggestionPopup && closeSuggestion && popupMessage) {
  const hideSuggestionPopup = () => {
    suggestionPopup.hidden = true;
  };

  const showPopup = (message) => {
    popupMessage.textContent = message;
    suggestionPopup.hidden = false;
    window.clearTimeout(suggestionTimer);
    suggestionTimer = window.setTimeout(hideSuggestionPopup, 3200);
  };

  if (sendSuggestion) {
    sendSuggestion.addEventListener("click", () => {
      if (suggestionInput && suggestionInput.value.trim() === "") {
        showPopup("Dê uma sugestão");
        return;
      }

      showPopup("Sugestão enviada");
    });
  }

  downloadButtons.forEach((button) => {
    button.addEventListener("click", () => {
      showPopup("Livro baixado");
    });
  });

  closeSuggestion.addEventListener("click", () => {
    window.clearTimeout(suggestionTimer);
    hideSuggestionPopup();
  });
}
