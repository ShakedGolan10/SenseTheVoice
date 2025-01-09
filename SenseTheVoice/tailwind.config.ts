import { nextui } from '@nextui-org/react'
/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './lib/**/*.{js,ts,jsx,tsx,mdx}',
    "./node_modules/@nextui-org/theme/dist/**/*.{js,ts,jsx,tsx}"
  ],
  darkMode: 'class',
  theme: {
    extend: {
      fontSize: {
        'base': ['1rem', { lineHeight: '1.5rem' }], 
        'subHeader': ['1.4rem', {lineHeight: '1.6rem'}]
      },
      gridTemplateColumns: {
        'grid-large': '100px 1fr 100px',
        'grid-medium': '50px 1fr 50px',
        'grid-small': '1fr',
      },
      gridColumn: {
        'column-large': '2/3',
        'column-medium': '2/-1',
        'column-small|full': '1/-1',
      },
      screens: {
        'tablet': { 'max': '1025px' },
        'mobile': { 'max': '640px' },
        'smMobile': { 'max': '420px' },
        // => @media (max-width: 639px) { ... }
      },
      backgroundImage: {
        'bgc-light': 'linear-gradient(to left ,#f2b0bc, #b0d1f2)',
        'bgc-dark':
          'linear-gradient(33deg, rgba(10,6,68,1) 26%, rgba(69,10,10,1) 76%);',
      },

      colors: {
        'green': '#008000',
        'light-green': '#90EE90',
        'red': '#B22222',
        'app-red': '#f2b0bc',
        'app-blue': '#b0d1f2',

      },
      keyframes: {
        scrollMessages: {
          '0%': { transform: 'translateY(0)' },
          // '25%': { transform: 'translateY(-25%)' },
          '50%': { transform: 'translateY(-100%)' },
          // '75%': { transform: 'translateY(50%)' },
          '100%': { transform: 'translateY(100%)' },
        }
      },
      animation: {
        scrollMsg: 'scrollMessages 10s linear infinite'
      },

    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    nextui({
      themes: {
        light: {
          layout: {},
          colors: {},
        },
        dark: {
          layout: {},
          colors: {
            foreground: '#FFFFFF',
          },
        },
        'light-desktop': {
          extend: 'light',
          colors: {},          
          layout: {
            fontSize: {
              large: '3.5rem',
              medium: '2.75rem',
            },
            lineHeight: {
              large: '4.5rem',
              medium: '3.25rem',
            }
          },
        },
        'light-tablet': {
          extend: 'light',
          colors: {},
          layout: {
            fontSize: {
              large: '2.75rem',
              medium: '2rem',
            },
            lineHeight: {
              large: '3.5rem',
              medium: '2.75rem',
            }
          },
        },
        'light-mobile': {
          extend: 'light',
          colors: {},
          layout: {
            fontSize: {
              large: '2.25rem',
              medium: '1.8rem',
            },
            lineHeight: {
              large: '2.75rem',
              medium: '2.25rem',
            }
          },
        },
        'dark-desktop': {
          extend: 'dark',
          colors: {},
          layout: {
            fontSize: {
              large: '3.5rem',
              medium: '2.75rem',
            },
            lineHeight: {
              large: '4.5rem',
              medium: '3.25rem',
            }
          },
        },
        'dark-tablet': {
          extend: 'dark',
          colors: {},
          layout: {
            fontSize: {
              large: '2.75rem',
              medium: '2rem',
            },
            lineHeight: {
              large: '3.5rem',
              medium: '2.75rem',
            }
          },
        },
        'dark-mobile': {
          extend: 'dark',
          colors: {},
          layout: {
            fontSize: {
              large: '2.25rem',
              medium: '1.8rem',
            },
            lineHeight: {
              large: '2.75rem',
              medium: '2.25rem',
            }
          },
        },
      },
    }),
  ],
}

