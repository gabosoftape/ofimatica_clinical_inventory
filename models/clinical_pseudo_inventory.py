
from odoo import api, fields, models, _

class pseudoInventory(models.Model):
    _name = 'historial.pseudoinventario'
    _description = 'Inventario'
    _rec_name = 'folio'

    folio = fields.Char('ID', size=128)
    categoria = fields.Char("Categoria")
    sku = fields.Char("SKU Codigo de Barras")
    articulo = fields.Char("Articulo")
    familia = fields.Char("Familia")
    descripcion = fields.Char("Descripcion")
    fecha_inv = fields.Date("Fecha de inventario")
    fecha_ven = fields.Date("Fecha de Vencimiento")
    registro = fields.Char("Registro")
    lote = fields.Char("Lote")
    caracteristicas = fields.Char("Caracteristicas")
    color = fields.Char("Color")
    poder = fields.Char("Poder")
    precio1 = fields.Char("Precio 1")
    precio2 = fields.Char("Precio 2")
    precio3 = fields.Char("Precio 3")
    ubicacion1 = fields.Char("Ubicacion 1")
    ubicacion2 = fields.Char("Ubicacion 2")
    ubicacion3 = fields.Char("Ubicacion 3")
    cantidades = fields.Float("Cantidades")
    proveedor = fields.Char("Proveedor")
    fecha_compra = fields.Date("Fecha de Compra")
    fecha_ven2 = fields.Date("Fecha de Vencimiento 2")
    factura_compra_proveedor = fields.Date("Factura Compra Proveedor")
    nit = fields.Char("NIT")
    nombre = fields.Char("Nombre")
    contacto = fields.Char("Nombre Contacto")
    ciudad = fields.Char("Ciudad de proveedor")
    direccion = fields.Char("Direccion")
    email = fields.Char("Email")
    celular = fields.Char("Celular")
    telefono = fields.Char("Telefono")
    notas = fields.Text("Notas y Observaciones del proveedor")
    cantidad = fields.Float("Cantidad")
    sede_in = fields.Char("Sede destino")
    sede_out = fields.Char("Sede salida")


    @api.model
    def create(self, vals):
        number = self.env['ir.sequence'].next_by_code('historial.pseudoinventario')
        vals['folio'] = str(number)
        result = super(pseudoInventory, self).create(vals)
        return result