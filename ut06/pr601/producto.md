# GESTION_PRODUCTOS

### Antes de nada siempre descomento el fichero access en manifest.
## init.py

```python
from . import producto
```

## Producto

 ```python
# -*- coding: utf-8 -*-
from odoo import models, fields, api

class producto(models.Model):
    _name = 'gestion_productos.producto'
    _description = 'Modulo de gestion de productos'

    nombre = fields.Char(string='Nombre del Producto')
    descripcion = fields.Text(string='Descripción del Producto')
    codigo = fields.Char(string='Código de Producto', required=True)
    imagen = fields.Image(string='Imagen del Producto')

    
    categoria = fields.Selection([
        ('jardin', 'Jardín'),
        ('hogar', 'Hogar'),
        ('electrodomesticos', 'Electrodomésticos')
    ], string='Categoría', required=True)
    
    destacable = fields.Boolean(string='Producto Destacable', default=False)

    precio_venta = fields.Float(string='Precio de Venta')
    stock_disponible = fields.Integer(string='Stock Disponible')
    
    fecha_creacion = fields.Datetime(string='Fecha de Creación', default=fields.Date.today)
    fecha_actualizacion = fields.Datetime(string='Fecha de Última Actualización')

    
    activo = fields.Boolean(string='Activo', default=True)
    peso = fields.Float(string='Peso del Producto', digits=(6, 2))

 ```

## ir.model.access.csv

 ```css
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_gestion_productos_producto,gestion_productos.producto,model_gestion_productos_producto,base.group_user,1,1,1,1
```
## views.xml

```xml
<odoo>
  <data>
    <!-- explicit list view definition -->

    <record model="ir.ui.view" id="gestion_productos.list">
      <field name="name">gestion_productos list</field>
      <field name="model">gestion_productos.producto</field>
      <field name="arch" type="xml">
        <tree>
          <field name="nombre"/>
          <field name="descripcion"/>
          <field name="codigo"/>
          <field name="imagen"/>
          <field name="categoria"/>
          <field name="destacable"/>
          <field name="precio_venta"/>
          <field name="stock_disponible"/>
          <field name="fecha_creacion"/>
          <field name="fecha_actualizacion"/>
          <field name="activo"/>
          <field name="peso"/>
        </tree>
      </field>
    </record>


    <!-- actions opening views on models -->

    <record model="ir.actions.act_window" id="gestion_productos.action_window">
      <field name="name">gestion_productos window</field>
      <field name="res_model">gestion_productos.producto</field>
      <field name="view_mode">tree,form</field>
    </record>



    <!-- Top menu item -->

    <menuitem name="gestion_productos" id="gestion_productos.menu_root"/>

    <!-- menu categories -->

    <menuitem name="Productos" id="gestion_productos.menu_1" parent="gestion_productos.menu_root"/>

    <menuitem name="Lista de Productos" id="gestion_productos.menu_1_list" parent="gestion_productos.menu_1"
              action="gestion_productos.action_window"/>
  
  </data>
</odoo>
```
![](productos.png "Captura del modulo productos")