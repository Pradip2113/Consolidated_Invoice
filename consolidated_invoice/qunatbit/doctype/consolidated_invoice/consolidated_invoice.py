# Copyright (c) 2023, Abhishek and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ConsolidatedInvoice(Document):
		@frappe.whitelist()
		def get_item(self):
			doc=frappe.db.get_list('Sales Invoice')
			for d in doc:
				doc1=frappe.get_doc('Sales Invoice',d.name)
				if(self.customer==doc1.customer):
					for d1 in doc1.get("items"):	
						if(doc1.count!="1"):

							self.append("items",{
									"item_name":"{0}:{1}".format(d1.item_code,d1.item_name),
									"qty":d1.qty,
									"rate":d1.rate,
									"amount":d1.amount,
									"description":d1.description,
									"uom":d1.uom,
									"conversion_factor":d1.conversion_factor,
									"rate":d1.rate,
									"base_rate":d1.base_rate,
									"base_amount":d1.base_amount,
									"document_name":d.name,

									"customer_item_code":d.customer_item_code,
									"item_group":d.item_group,
									"brand":d.brand,
									"image":d.image,
									"image_view":d.image_view,
									"stock_uom":d.stock_uom,
									"uom":d.uom,
									"conversion_factor":d.conversion_factor,
									"stock_qty":d.stock_qty,
									"price_list_rate":d.price_list_rate,
									"base_price_list_rate":d.base_price_list_rate,
									"margin_type":d.margin_type,
									"margin_rate_or_amount":d.margin_rate_or_amount,
									"rate_with_margin":d.rate_with_margin,
									"discount_percentage":d.discount_percentage,
									"discount_amount":d.discount_amount,
									"base_rate_with_margin":d.base_rate_with_margin,
									"item_tax_template":d.item_tax_template,
									"base_rate":d.base_rate,
									"base_amount":d.base_amount,
									"pricing_rules":d.pricing_rules,
									"stock_uom_rate":d.stock_uom_rate,
									"is_free_item":d.is_free_item,
									"grant_commission":d.grant_commission,
									"net_rate":d.net_rate,
									"net_amount":d.net_amount,
									"base_net_rate":d.base_net_rate,
									"base_net_amount":d.base_net_amount,
									"delivered_by_supplier":d.delivered_by_supplier,
									"accounting":d.accounting,
									"income_account":d.income_account,
									"is_fixed_asset":d.is_fixed_asset,
									"asset":d.asset,
									"finance_book":d.finance_book,
									"expense_account":d.expense_account,
									"discount_account":d.discount_account,
									"deferred_revenue_account":d.deferred_revenue_account,
									"service_stop_date":d.service_stop_date,
									"enable_deferred_revenue":d.enable_deferred_revenue,
									"service_start_date":d.service_start_date,
									"service_end_date":d.service_end_date,
									"weight_per_unit":d.weight_per_unit,
									"total_weight":d.total_weight,
									"weight_uom":d.weight_uom,
									"warehouse":d.warehouse,
									"target_warehouse":d.target_warehouse,
									"quality_inspection":d.quality_inspection,
									"batch_no":d.batch_no,
									"incoming_rate":d.incoming_rate,
									"allow_zero_valuation_rate":d.allow_zero_valuation_rate,
									"serial_no":d.serial_no,
									"item_tax_rate":d.item_tax_rate,
									"actual_batch_qty":d.actual_batch_qty,
									"actual_qty":d.actual_qty,
									"sales_order":d.sales_order,
									"so_detail":d.so_detail,
									"sales_invoice_item":d.sales_invoice_item,
									"delivery_note":d.delivery_note,
									"dn_detail":d.dn_detail,
									"delivered_qty":d.delivered_qty,
									"purchase_order":d.purchase_order,
									"purchase_order_item":d.purchase_order_item,
									"cost_center":d.cost_center,
									"project":d.project,
									"page_break":d.page_break
									}
								)
							qt=0
							amt=0
							for d3 in self.get("items"):
									qt=qt+d3.qty
									amt=amt+d3.amount
							self.total_qty=qt
							self.total=amt
						
								
		def before_save(self):
			count="1"
			for d3 in self.get("items"):
				documentname=d3.document_name
				doc1=frappe.get_doc('Sales Invoice',documentname)
				if(self.customer==doc1.customer):
					frappe.db.set_value(
						"Sales Invoice", documentname,"count",count
					)
				

		def on_cancel(self):
			count="0"
			for i in self.get("items"):
				doc = frappe.db.get_list("Sales Invoice")
				for d in doc:
					d1 = frappe.get_doc("Sales Invoice", d.name)
					if(i.document_name == d.name):
						frappe.db.set_value(
							"Sales Invoice", d.name,"count",count
						)

		
			
