<template>
  <v-app>
    <v-container>
      <v-card class="mx-auto my-10" color="indigo-darken-2" min-width="200" max-width="500" min-height="300">
        <v-switch class="position-absolute left-0 top-0 ml-4" v-model="isLlama" color="secondary"
          :label="isLlama ? 'Llama3' : 'DeepSeek'" v-slot:prepend="stuff" />
        <v-card v-if="loading" class="my-2" color="tertiary">
          <v-progress-linear class="" indeterminate />
        </v-card>
        <v-virtual-scroll ref="virtualScroller" class="mt-10 ma-5" height="190" :items="chatMessages">
          <template v-slot:default="{ item }">
            <v-card :class="`my-2 ${item.isUser ? 'ml-20' : 'mr-20'}`" :color="item.isUser ? 'secondary' : 'tertiary'">
              <v-card-text>{{ item.message }}</v-card-text>
            </v-card>
          </template>
        </v-virtual-scroll>
        <v-text-field :label="`Message ${isLlama ? 'Llama3' : 'DeepSeek'}`" auto-focus hide-details
          class="position-absolute bottom-0 left-0 right-0 ma-2" variant="solo" bg-color="indigo-lighten-1"
          v-model="message" @update:focused="(value: boolean) => isFocused = value"></v-text-field>
      </v-card>

    </v-container>
  </v-app>
</template>


<script setup lang="ts">
import axios from 'axios';
import { VVirtualScroll } from 'vuetify/components';

const message = ref("");
const isFocused = ref(true);
const isLlama = ref(true);
const chatMessages = ref<Array<Message>>([]);
const virtualScroller = ref<VVirtualScroll>(null!);
const loading = ref(false);

onMounted(() => {
  window.addEventListener("keyup", onKeyup);
});

onUnmounted(() => {
  window.removeEventListener("keyup", onKeyup);
});

async function onKeyup(event: KeyboardEvent) {
  if (event.key === "Enter" && isFocused.value) {
    let newMessage = new Message(message.value, true);
    message.value = "";
    chatMessages.value.push(newMessage);
    loading.value = true;
    await sendMessage();
    virtualScroller.value.scrollToIndex(chatMessages.value.length + 1);
  }
}

async function sendMessage() {
  try {
    let message = chatMessages.value[chatMessages.value.length - 1].message;
    let url = 'http://backend:5000/chat';
    let response = await axios.get(url, {
      params: {
        message: message,
        isLlama: isLlama.value,
      }
    });
    let newMessage = new Message(response.data, false);
    chatMessages.value.push(newMessage);
  } catch (error) {
    console.error(`Error querying LLM: ${error}`);
  }
  loading.value = false;
}

class Message {
  message: string;
  isUser: boolean;

  constructor(message: string, isUser: boolean) {
    this.message = message;
    this.isUser = isUser;
  }

}
</script>