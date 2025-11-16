from django.db import models

class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100, verbose_name="Nombre de la Empresa")
    contacto = models.CharField(max_length=100, verbose_name="Persona de Contacto")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Email")
    direccion = models.TextField(verbose_name="Dirección")
    rfc = models.CharField(max_length=13, verbose_name="RFC")
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha de Registro")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
    
    def __str__(self):
        return self.nombre_empresa



class Empleado(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    puesto = models.CharField(max_length=50, verbose_name="Puesto")
    fecha_contratacion = models.DateField(verbose_name="Fecha de Contratación")
    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salario")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Email")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: Cliente
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    registrado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================

# MODELO: Medicamento
# ==========================================
class Medicamento(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    laboratorio = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField()
    codigo_barras = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción")
    categoria = models.CharField(max_length=50, verbose_name="Categoría")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name="Proveedor")
    codigo_barras = models.CharField(max_length=50, verbose_name="Código de Barras")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Actualizado")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: Venta
# ==========================================
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')  # 1 a muchos
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True)
    medicamentos = models.ManyToManyField(Medicamento, related_name='ventas')
    productos = models.ManyToManyField(Producto, related_name='ventas')
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, choices=[
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
        ('TRANSFERENCIA', 'Transferencia'),
    ])
    numero_factura = models.CharField(max_length=20, unique=True)
    observaciones = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, default='COMPLETADA', choices=[
        ('COMPLETADA', 'Completada'),
        ('PENDIENTE', 'Pendiente'),
        ('CANCELADA', 'Cancelada'),
    ])

