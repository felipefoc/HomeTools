<template>
  <button class="card card-stats card-amazing" @click="$emit('click')">
    <div class="row">
      <div class="col text-center">
        <div class="numbers">
          <slot name="content"></slot>
        </div>
      </div>
    </div>
  </button>
</template>
<script>
  import Card from './Card.vue'
  export default {
    name: 'stats-card',
    components: {
      Card
    },
    emits: ['click']
  }
</script>
<style scoped>
  button.card-amazing {
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
  }

  button.card.card-amazing {
    background-color: var(--white);
    border: 1px solid var(--light-border-color);
    border-radius: 6px;
    cursor: pointer;
    padding: 1.25rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) ease;
    width: 100%;
  }

  button.card.card-amazing:hover,
  button.card.card-amazing:active {
    transform: scale(1.05);
    transition-duration: 0.1s;
  }

  button.card.card-amazing:active {
    transition-duration: 0s;
  }

  .numbers {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
  }
</style>


