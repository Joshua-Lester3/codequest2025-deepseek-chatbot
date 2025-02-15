// import this after install `@mdi/font` package
import '@mdi/font/css/materialdesignicons.css';

import 'vuetify/styles';
import { createVuetify, type ThemeDefinition } from 'vuetify';

const defaultTheme: ThemeDefinition = {
  dark: false,
  colors: {
    background: '#C5CAE9',
    primary: '#303F9F',
    secondary: '#5C6BC0',
    tertiary: '#1A237E',
    error: '#B00020',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FB8C00',
  },
};

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    // ... your configuration
    theme: {
      defaultTheme: 'defaultTheme',
      themes: {
        defaultTheme,
      },
    },
  });
  app.vueApp.use(vuetify);
});
