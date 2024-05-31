odoo.define("pos_discount_validation.NumpadWidget", function (require) {
  "use strict";

  const NumpadWidget = require("point_of_sale.NumpadWidget");
  const Registries = require("point_of_sale.Registries");
  const ProtectedDiscountButton = (NumpadWidget) =>
    class extends NumpadWidget {
      async changeMode(mode) {
        if (mode === "discount") {
          // Show password popup
          const { confirmed, payload } = await this.showPopup("TextAreaPopup", {
            title: this.env._t("Enter Password"),
            body: this.env._t("Please enter the password to apply a discount."),
            confirmText: this.env._t("Apply"),
            cancelText: this.env._t("Cancel"),
            input: "password",
          });
          if (confirmed && payload === "admin") {
            super.changeMode(mode);
          } else {
            this.showPopup("ErrorPopup", {
              title: this.env._t("Invalid Password"),
              body: this.env._t("The password you entered is incorrect."),
            });
          }
        } else {
          super.changeMode(mode);
        }
      }
    };

  Registries.Component.extend(NumpadWidget, ProtectedDiscountButton);

  return NumpadWidget;
});
