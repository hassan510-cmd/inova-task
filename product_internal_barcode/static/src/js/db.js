odoo.define("product_internal_barcode.DB", function (require) {
  "use strict";

  var PosDB = require("point_of_sale.DB");

  PosDB.include({
    _product_search_string: function (product) {
      var str = this._super(product);
      if (product.internal_barcode) {
        str = str.replace(/[\n]/, "|" + product.internal_barcode + "\n");
      }
      return str;
    },
  });
});
