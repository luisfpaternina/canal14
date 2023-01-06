odoo.define('js_pos.PaymentScreenButton', function(require) {
'use strict';

   const { Gui } = require('point_of_sale.Gui');
   const PosComponent = require('point_of_sale.PosComponent');
   const { posbus } = require('point_of_sale.utils');
   const ProductScreen = require('point_of_sale.ProductScreen');
   const { useListener } = require('web.custom_hooks');
   const Registries = require('point_of_sale.Registries');
   const PaymentScreen = require('point_of_sale.PaymentScreen');
    const CustomButtonPaymentScreen = (PaymentScreen) =>
       class extends PaymentScreen {
           constructor() {
               super(...arguments);
           }
           IsCustomButton() {
                Gui.showPopup("ErrorPopup", {
                       title: this.env._t('POPUP DE ALERTA'),
                       body: this.env._t('PRUEBA DE BOTON EN PAGOS LFPV'),
                   });
           }
       };
   Registries.Component.extend(PaymentScreen, CustomButtonPaymentScreen);
   return CustomButtonPaymentScreen;
});
