/* global Backbone, waitForWebfonts */
odoo.define('point_of_sale.models_inherit', function (require) {
    "use strict";
    var models = require('point_of_sale.models');

    var existing_models = models.PosModel.prototype.models;
    var product_index = _.findIndex(existing_models, function (model) {
        return model.model === "product.product";
    });
    var product_model = existing_models[product_index];
    product_model.domain = function (self) {
        var domain = ['&', '&', ['sale_ok','=',true],['available_in_pos','=',true],'|',['company_id','=',self.config.company_id[0]],['company_id','=',false]];
        if (self.config.point_qty_available_id) {
            let pqa_num = 1;
            if(self.config.point_qty_available_num > 1) {
                pqa_num = self.config.point_qty_available_num;
            }
            domain.splice(4, 0, ['qty_available','>=',pqa_num]);
        }
        if (self.config.limit_categories && self.config.iface_available_categ_ids.length) {
            domain.unshift('&');
            domain.push(['pos_categ_id', 'in', self.config.iface_available_categ_ids]);
        }
        if (self.config.iface_tipproduct) {
            domain.unshift(['id', '=', self.config.tip_product_id[0]]);
            domain.unshift('|');
        }
        return domain;
    }
})