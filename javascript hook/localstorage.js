// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.maersk.com.cn/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    /**
  * 重写localStorage
  */
    function rewriteLocalStorage () {
      if (!window.__rewrite__localStorage) {
        Object.assign(window, {
          __rewrite__localStorage: true,
          __localStorage__setItem: localStorage.setItem,
          __localStorage__getItem: localStorage.getItem,
          __localStorage__removeItem: localStorage.removeItem
        })

        if (!localStorage.__expires) {
          localStorage.__expires = '{}'
        }

        localStorage.setItem = function (key, value, millisecond) {
          console.log(key);
          if(key === 'frJwt'){
              debugger;

          }
          if (millisecond) {
            let __expires = JSON.parse(localStorage.__expires)
            __expires[key] = +Date.now() + millisecond
            localStorage.__expires = JSON.stringify(__expires)
          }
          window.__localStorage__setItem.call(this, key, value)
        }

        localStorage.getItem = function (key) {
          window.clearExpires()
          return window.__localStorage__getItem.call(this, key)
        }

        localStorage.removeItem = function (key) {
          let __expires = JSON.parse(localStorage.__expires)
          delete __expires[key]
          localStorage.__expires = JSON.stringify(__expires)
          return window.__localStorage__removeItem.call(this, key)
        }

        window.clearExpires = function () {
          let __expires = JSON.parse(localStorage.__expires)
          for (let key in __expires) {
            if (__expires[key] < Date.now()) {
              localStorage.removeItem(key)
            }
          }
        }
      }
    }
    rewriteLocalStorage();
})();