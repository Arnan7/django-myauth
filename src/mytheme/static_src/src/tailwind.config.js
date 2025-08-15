// tailwind.config.js
module.exports = {
  content: [
    '../../../../templates/**/*.html', // Esta es la ruta correcta
    '../../../../**/templates/**/*.html', // Esta línea también es correcta y más flexible
    '../../../../myauthapp/templates/**/*.html',
    '../../../../project_auth_app/templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}