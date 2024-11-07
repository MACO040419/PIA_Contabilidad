def presupuesto_ventas():
    print(f'''
{'-' * 88}
{'PRESUPUESTO DE VENTAS':^88}
{'-' * 88}
{'':<30} {'1er. Semestre':^20} {'2do. Semestre':^20} {'2016':^10}
{'-' * 88}
{'Producto 1':<30}
{'Unidades a vender':<30} {ventasPlaneadasPrimerSemestre_producto1:^20,} {ventasPlaneadasSegundoSemestre_producto1:^20,} 
{'Precio de venta':<30} ${precioVentasPrimerSemestre_producto1:^19,.2f} ${precioVentasSegundoSemestre_producto1:^19,.2f}
{'Importe de venta':<30} ${ventasPlaneadasPrimerSemestre_producto1 * precioVentasPrimerSemestre_producto1:^19,.2f} ${ventasPlaneadasSegundoSemestre_producto1 * precioVentasSegundoSemestre_producto1:^19,.2f} ${(ventasPlaneadasPrimerSemestre_producto1 * precioVentasPrimerSemestre_producto1) + (ventasPlaneadasSegundoSemestre_producto1 * precioVentasSegundoSemestre_producto1):^9,.2f}
{'-' * 88}
{'Producto 2':<30}
{'Unidades a vender':<30} {ventasPlaneadasPrimerSemestre_producto2:^20,} {ventasPlaneadasSegundoSemestre_producto2:^20,}
{'Precio de venta':<30} ${precioVentasPrimerSemestre_producto2:^19,.2f} ${precioVentasSegundoSemestre_producto2:^19,.2f}
{'Importe de venta':<30} ${ventasPlaneadasPrimerSemestre_producto2 * precioVentasPrimerSemestre_producto2:^19,.2f} ${ventasPlaneadasSegundoSemestre_producto2 * precioVentasSegundoSemestre_producto2:^19,.2f} ${(ventasPlaneadasPrimerSemestre_producto2 * precioVentasPrimerSemestre_producto2)+(ventasPlaneadasSegundoSemestre_producto2 * precioVentasSegundoSemestre_producto2):^9,.2f}
{'-' * 88}
{'Producto 2':<30}
{'Unidades a vender':<30} {ventasPlaneadasPrimerSemestre_producto3:^20,} {ventasPlaneadasSegundoSemestre_producto3:^20,}
{'Precio de venta':<30} ${precioVentasPrimerSemestre_producto3:^19,.2f} ${precioVentasSegundoSemestre_producto3:^19,.2f}
{'Importe de venta':<30} ${ventasPlaneadasPrimerSemestre_producto3 * precioVentasPrimerSemestre_producto3:^19,.2f} ${ventasPlaneadasSegundoSemestre_producto3 * precioVentasSegundoSemestre_producto3:^19,.2f} ${(ventasPlaneadasPrimerSemestre_producto3 * precioVentasPrimerSemestre_producto3)+(ventasPlaneadasSegundoSemestre_producto3 * precioVentasSegundoSemestre_producto3):^9,.2f}
{'-' * 88}
{'Total de ventas x Semestre':<30} ${(ventasPlaneadasPrimerSemestre_producto1 * precioVentasPrimerSemestre_producto1) + (ventasPlaneadasPrimerSemestre_producto2 * precioVentasPrimerSemestre_producto2) + (ventasPlaneadasPrimerSemestre_producto3 * precioVentasPrimerSemestre_producto3):^19,.2f} ${(ventasPlaneadasSegundoSemestre_producto1 * precioVentasSegundoSemestre_producto1)+(ventasPlaneadasPrimerSemestre_producto2 * precioVentasPrimerSemestre_producto2)+(ventasPlaneadasSegundoSemestre_producto3 * precioVentasSegundoSemestre_producto3):^19,.2f} ${((ventasPlaneadasPrimerSemestre_producto1 * precioVentasPrimerSemestre_producto1) + (ventasPlaneadasSegundoSemestre_producto1 * precioVentasSegundoSemestre_producto1))+ (ventasPlaneadasPrimerSemestre_producto2 * precioVentasPrimerSemestre_producto2)+(ventasPlaneadasSegundoSemestre_producto2 * precioVentasSegundoSemestre_producto2)+(ventasPlaneadasPrimerSemestre_producto3 * precioVentasPrimerSemestre_producto3)+(ventasPlaneadasSegundoSemestre_producto3 * precioVentasSegundoSemestre_producto3):^9,.2f}
{'-' * 88}
''')
    
def determinacion_saldo_de_clientes_flujo_de_entradas():
    print(f'''
{'-' * 70}
{'DETERMINACION DEL SALDO DE CLIENTES Y FLUJO DE ENTRADAS':^70}
{'-' * 70}
{'Descripcion':<30} {'Importe':^20} {'Total':^20}
{'Saldo de clientes':<30} {'':^20} ${clientes:^19,.2f}
{'Ventas 2016':<30} {'':^20} ${((ventasPlaneadasPrimerSemestre_producto1 * precioVentasPrimerSemestre_producto1) + (ventasPlaneadasSegundoSemestre_producto1 * precioVentasSegundoSemestre_producto1)) + (ventasPlaneadasPrimerSemestre_producto2 * precioVentasPrimerSemestre_producto2) + (ventasPlaneadasSegundoSemestre_producto2 * precioVentasSegundoSemestre_producto2) + (ventasPlaneadasPrimerSemestre_producto3 * precioVentasPrimerSemestre_producto3) + (ventasPlaneadasSegundoSemestre_producto3 * precioVentasSegundoSemestre_producto3):^19,.2f}
{'Total de clientes 2016':<30} {'':^20} ${clientes + ((ventasPlaneadasPrimerSemestre_producto1 * precioVentasPrimerSemestre_producto1) + (ventasPlaneadasSegundoSemestre_producto1 * precioVentasSegundoSemestre_producto1)) + (ventasPlaneadasPrimerSemestre_producto2 * precioVentasPrimerSemestre_producto2) + (ventasPlaneadasSegundoSemestre_producto2 * precioVentasSegundoSemestre_producto2) + (ventasPlaneadasPrimerSemestre_producto3 * precioVentasPrimerSemestre_producto3) + (ventasPlaneadasSegundoSemestre_producto3 * precioVentasSegundoSemestre_producto3):^19,.2f}

{'Entradas de efectivo':<30}
{'Por cobranza del 2015 (100%)':<30} ${clientes * proveedores2015_pago:^19,.2f}
{'Por cobranza del 2016 (80%)':<30} ${(((ventasPlaneadasPrimerSemestre_producto1 * precioVentasPrimerSemestre_producto1) + (ventasPlaneadasSegundoSemestre_producto1 * precioVentasSegundoSemestre_producto1)) + ((ventasPlaneadasPrimerSemestre_producto2 * precioVentasPrimerSemestre_producto2) + (ventasPlaneadasSegundoSemestre_producto2 * precioVentasSegundoSemestre_producto2)) + ((ventasPlaneadasPrimerSemestre_producto3 * precioVentasPrimerSemestre_producto3) + (ventasPlaneadasSegundoSemestre_producto3 * precioVentasSegundoSemestre_producto3))) * ventasPresupuestadas_cobro:^19,.2f}
{'':<30} {'':^20} ${(clientes * proveedores2015_pago) + (((ventasPlaneadasPrimerSemestre_producto1 * precioVentasPrimerSemestre_producto1) + (ventasPlaneadasSegundoSemestre_producto1 * precioVentasSegundoSemestre_producto1)) + ((ventasPlaneadasPrimerSemestre_producto2 * precioVentasPrimerSemestre_producto2) + (ventasPlaneadasSegundoSemestre_producto2 * precioVentasSegundoSemestre_producto2)) + ((ventasPlaneadasPrimerSemestre_producto3 * precioVentasPrimerSemestre_producto3) + (ventasPlaneadasSegundoSemestre_producto3 * precioVentasSegundoSemestre_producto3))) * ventasPresupuestadas_cobro:^19,.2f}

{'Saldo de clientes 2016':<30} {'':^20} ${clientes + ((ventasPlaneadasPrimerSemestre_producto1 * precioVentasPrimerSemestre_producto1) + (ventasPlaneadasSegundoSemestre_producto1 * precioVentasSegundoSemestre_producto1)) + (ventasPlaneadasPrimerSemestre_producto2 * precioVentasPrimerSemestre_producto2) + (ventasPlaneadasSegundoSemestre_producto2 * precioVentasSegundoSemestre_producto2) + (ventasPlaneadasPrimerSemestre_producto3 * precioVentasPrimerSemestre_producto3) + (ventasPlaneadasSegundoSemestre_producto3 * precioVentasSegundoSemestre_producto3)-((clientes * proveedores2015_pago) + (((ventasPlaneadasPrimerSemestre_producto1 * precioVentasPrimerSemestre_producto1) + (ventasPlaneadasSegundoSemestre_producto1 * precioVentasSegundoSemestre_producto1)) + ((ventasPlaneadasPrimerSemestre_producto2 * precioVentasPrimerSemestre_producto2) + (ventasPlaneadasSegundoSemestre_producto2 * precioVentasSegundoSemestre_producto2)) + ((ventasPlaneadasPrimerSemestre_producto3 * precioVentasPrimerSemestre_producto3) + (ventasPlaneadasSegundoSemestre_producto3 * precioVentasSegundoSemestre_producto3))) * ventasPresupuestadas_cobro):^19,.2f}
{'-' * 70}
''')

def presupuesto_de_produccion():
    print(f'''
{'-' * 90}
{'PRESUPUESTO DE PRODUCCION':^90}
{'-' * 90}
{'':^30} {'1er Semestre':^20} {'2do Semestre':^20} {'Total 2016':^20}
{'-' * 90}
{'Producto 1':<30}
{'Unidades a vender':<30} {ventasPlaneadasPrimerSemestre_producto1:^20,} {ventasPlaneadasSegundoSemestre_producto1:^20,} {ventasPlaneadasPrimerSemestre_producto1+ventasPlaneadasSegundoSemestre_producto1:^20,}
{'Inventario final':<30} {producto1_inventarioInicialPrimerSemestre:^20,} {producto1_inventarioFinalSegundoSemestre:^20,} {producto1_inventarioFinalSegundoSemestre:^20,}
{'Total de unidades':<30} {ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre:^20,} {ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre:^20,} {(ventasPlaneadasPrimerSemestre_producto1+ventasPlaneadasSegundoSemestre_producto1)+(producto1_inventarioFinalSegundoSemestre):^20,}
{'Inventario inicial':<30} {producto1_inventarioInicialPrimerSemestre:^20,} {producto1_inventarioInicialPrimerSemestre:^20,} {producto1_inventarioInicialPrimerSemestre:^20,}
{'Unidades a produccir':<30} {(ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre):^20,} {(ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre):^20,} {((ventasPlaneadasPrimerSemestre_producto1+ventasPlaneadasSegundoSemestre_producto1)+(producto1_inventarioFinalSegundoSemestre))-(producto1_inventarioInicialPrimerSemestre):^20,}
{'-' * 90}
{'Producto 2':<30}
{'Unidades a vender':<30} {ventasPlaneadasPrimerSemestre_producto2:^20,} {ventasPlaneadasSegundoSemestre_producto2:^20,} {ventasPlaneadasPrimerSemestre_producto2+ventasPlaneadasSegundoSemestre_producto2:^20,}
{'Inventario final':<30} {producto2_inventarioInicialPrimerSemestre:^20,} {producto2_inventarioFinalSegundoSemestre:^20,} {producto2_inventarioFinalSegundoSemestre:^20,}
{'Total de unidades':<30} {ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre:^20,} {ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre:^20,} {(ventasPlaneadasPrimerSemestre_producto2+ventasPlaneadasSegundoSemestre_producto2)+(producto2_inventarioFinalSegundoSemestre):^20,}
{'Inventario inicial':<30} {producto2_inventarioInicialPrimerSemestre:^20,} {producto2_inventarioInicialPrimerSemestre:^20,} {producto2_inventarioInicialPrimerSemestre:^20,}
{'Unidades a produccir':<30} {(ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre):^20,} {(ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre):^20,} {((ventasPlaneadasPrimerSemestre_producto2+ventasPlaneadasSegundoSemestre_producto2)+(producto2_inventarioFinalSegundoSemestre))-(producto2_inventarioInicialPrimerSemestre):^20,}
{'-' * 90}
{'Producto 3':<30}
{'Unidades a vender':<30} {ventasPlaneadasPrimerSemestre_producto3:^20,} {ventasPlaneadasSegundoSemestre_producto3:^20,} {ventasPlaneadasPrimerSemestre_producto3+ventasPlaneadasSegundoSemestre_producto3:^20,}
{'Inventario final':<30} {producto3_inventarioInicialPrimerSemestre:^20,} {producto3_inventarioFinalSegundoSemestre:^20,} {producto3_inventarioFinalSegundoSemestre:^20,}
{'Total de unidades':<30} {ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre:^20,} {ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre:^20,} {(ventasPlaneadasPrimerSemestre_producto3+ventasPlaneadasSegundoSemestre_producto3)+(producto3_inventarioFinalSegundoSemestre):^20,}
{'Inventario inicial':<30} {producto3_inventarioInicialPrimerSemestre:^20,} {producto3_inventarioInicialPrimerSemestre:^20,} {producto3_inventarioInicialPrimerSemestre:^20,}
{'Unidades a produccir':<30} {(ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre):^20,} {(ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre):^20,} {((ventasPlaneadasPrimerSemestre_producto3+ventasPlaneadasSegundoSemestre_producto3)+(producto3_inventarioFinalSegundoSemestre))-(producto3_inventarioInicialPrimerSemestre):^20,}
{'-' * 90}
''')
    
def presupuesto_de_requerimiento_de_materiales():
    print(f'''
{'-' * 90}
{'PRESUPUESTO DE REQUERIMIENTOS DE MATERIALES':^90}
{'-' * 90}
{'':^30} {'1er Semestre':^20} {'2do Semestre':^20} {'Total 2016':^20}
{'-' * 90}
Producto 1
{'Unidades a producir':<30} {(ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre):^20,} {(ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre):^20,} {((ventasPlaneadasPrimerSemestre_producto1+ventasPlaneadasSegundoSemestre_producto1)+(producto1_inventarioFinalSegundoSemestre))-(producto1_inventarioInicialPrimerSemestre):^20,}

Material A
{'Requerimiento de material':<30} {materiaprimaAmetros_producto1:^20.1f} {materiaprimaAmetros_producto1:^20.1f} {materiaprimaAmetros_producto1:^20.1f}
{'Total de Material A Requerido':<30} {materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)):^20,} {materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)):^20,} {materiaprimaAmetros_producto1*(((ventasPlaneadasPrimerSemestre_producto1+ventasPlaneadasSegundoSemestre_producto1)+(producto1_inventarioFinalSegundoSemestre))-(producto1_inventarioInicialPrimerSemestre)):^20,}
Material B
{'Requerimiento de material':<30} {materiaprimaBmetros_producto1:^20.1f} {materiaprimaBmetros_producto1:^20.1f} {materiaprimaBmetros_producto1:^20.1f}
{'Total de Material B Requerido':<30} {materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)):^20,} {materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)):^20,} {materiaprimaBmetros_producto1*(((ventasPlaneadasPrimerSemestre_producto1+ventasPlaneadasSegundoSemestre_producto1)+(producto1_inventarioFinalSegundoSemestre))-(producto1_inventarioInicialPrimerSemestre)):^20,}
Material C
{'Requerimiento de material':<30} {materiaprimaCpiezas_producto1:^20.1f} {materiaprimaCpiezas_producto1:^20.1f} {materiaprimaCpiezas_producto1:^20.1f}
{'Total de Material C Requerido':<30} {materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)):^20,} {materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)):^20,} {materiaprimaCpiezas_producto1*(((ventasPlaneadasPrimerSemestre_producto1+ventasPlaneadasSegundoSemestre_producto1)+(producto1_inventarioFinalSegundoSemestre))-(producto1_inventarioInicialPrimerSemestre)):^20,}
{'-' * 90}
Producto 2
{'Unidades a producir':<30} {(ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre):^20,} {(ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre):^20,} {((ventasPlaneadasPrimerSemestre_producto2+ventasPlaneadasSegundoSemestre_producto2)+(producto2_inventarioFinalSegundoSemestre))-(producto2_inventarioInicialPrimerSemestre):^20,}

Material A
{'Requerimiento de material':<30} {materiaprimaAmetros_producto2:^20.1f} {materiaprimaAmetros_producto2:^20.1f} {materiaprimaAmetros_producto2:^20.1f}
{'Total de Material A Requerido':<30} {materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)):^20,} {materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)):^20,} {materiaprimaAmetros_producto2*(((ventasPlaneadasPrimerSemestre_producto2+ventasPlaneadasSegundoSemestre_producto2)+(producto2_inventarioFinalSegundoSemestre))-(producto2_inventarioInicialPrimerSemestre)):^20,}
Material B
{'Requerimiento de material':<30} {materiaprimaBmetros_producto2:^20.1f} {materiaprimaBmetros_producto2:^20.1f} {materiaprimaBmetros_producto2:^20.1f}
{'Total de Material B Requerido':<30} {materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)):^20,} {materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)):^20,} {materiaprimaBmetros_producto2*(((ventasPlaneadasPrimerSemestre_producto2+ventasPlaneadasSegundoSemestre_producto2)+(producto2_inventarioFinalSegundoSemestre))-(producto2_inventarioInicialPrimerSemestre)):^20,}
Material C
{'Requerimiento de material':<30} {materiaprimaCpiezas_producto2:^20.1f} {materiaprimaCpiezas_producto2:^20.1f} {materiaprimaCpiezas_producto2:^20.1f}
{'Total de Material C Requerido':<30} {materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)):^20,} {materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)):^20,} {materiaprimaCpiezas_producto2*(((ventasPlaneadasPrimerSemestre_producto2+ventasPlaneadasSegundoSemestre_producto2)+(producto2_inventarioFinalSegundoSemestre))-(producto2_inventarioInicialPrimerSemestre)):^20,}
{'-' * 90}
Producto 3
{'Unidades a producir':<30} {(ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre):^20,} {(ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre):^20,} {((ventasPlaneadasPrimerSemestre_producto3+ventasPlaneadasSegundoSemestre_producto3)+(producto3_inventarioFinalSegundoSemestre))-(producto3_inventarioInicialPrimerSemestre):^20,}

Material A
{'Requerimiento de material':<30} {materiaprimaAmetros_producto3:^20.1f} {materiaprimaAmetros_producto3:^20.1f} {materiaprimaAmetros_producto3:^20.1f}
{'Total de Material A Requerido':<30} {materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)):^20,} {materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)):^20,} {materiaprimaAmetros_producto3*(((ventasPlaneadasPrimerSemestre_producto3+ventasPlaneadasSegundoSemestre_producto3)+(producto3_inventarioFinalSegundoSemestre))-(producto3_inventarioInicialPrimerSemestre)):^20,}
Material B
{'Requerimiento de material':<30} {materiaprimaBmetros_producto3:^20.1f} {materiaprimaBmetros_producto3:^20.1f} {materiaprimaBmetros_producto3:^20.1f}
{'Total de Material B Requerido':<30} {materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)):^20,} {materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)):^20,} {materiaprimaBmetros_producto3*(((ventasPlaneadasPrimerSemestre_producto3+ventasPlaneadasSegundoSemestre_producto3)+(producto3_inventarioFinalSegundoSemestre))-(producto3_inventarioInicialPrimerSemestre)):^20,}
Material C
{'Requerimiento de material':<30} {materiaprimaCpiezas_producto3:^20.1f} {materiaprimaCpiezas_producto3:^20.1f} {materiaprimaCpiezas_producto3:^20.1f}
{'Total de Material C Requerido':<30} {materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)):^20,} {materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)):^20,} {materiaprimaCpiezas_producto3*(((ventasPlaneadasPrimerSemestre_producto3+ventasPlaneadasSegundoSemestre_producto3)+(producto3_inventarioFinalSegundoSemestre))-(producto3_inventarioInicialPrimerSemestre)):^20,}
{'-' * 90}
Total de requerimientos
{'Material A':<30} {(materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))):^20,}\
{(materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))):^20,}\
 {((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))\
                            +((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))):^20,}
{'Material B':<30} {(materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))):^20,}\
 {(materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))):^20,}\
 {((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))\
                            +((materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))):^20,}
{'Material C':<30} {(materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))):^20,}\
 {(materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))):^20,}\
 {((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))\
                            +((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))):^20,}
''')
    
def presupuesto_compra_materiales():
    print(f'''
{'-' * 90}
{'PRESUPUESTO DE COMPRA DE MATERIALES':^90}
{'-' * 90}
{'':^30} {'1er Semestre':^20} {'2do Semestre':^20} {'Total 2016':^20}
{'-' * 90}
Material A
{'Requerimiento de materiales':<30} {(materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))):^20,}\
{(materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))):^20,}\
 {((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))\
                            +((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))):^20,}
{'Inventario final':<30} {materiaprimaAmetros_inventarioInicialPrimerSemestre:^20,} {materiaprimaAmetros_inventarioFinalSegundoSemestre:^20,} {materiaprimaAmetros_inventarioFinalSegundoSemestre:^20,}
{'Total de materiales':<30} {(materiaprimaAmetros_inventarioInicialPrimerSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)))):^20,}\
{(materiaprimaAmetros_inventarioFinalSegundoSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))):^20,}\
{(materiaprimaAmetros_inventarioFinalSegundoSemestre)+(((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))\
                            +((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))):^20,}
{'Inventario Inicial':<30} {materiaprimaAmetros_inventarioInicialPrimerSemestre:^20,} {materiaprimaAmetros_inventarioInicialPrimerSemestre:^20,} {materiaprimaAmetros_inventarioInicialPrimerSemestre:^20,}
{'Material a comprar':<30} {(materiaprimaAmetros_inventarioInicialPrimerSemestre)-(materiaprimaAmetros_inventarioInicialPrimerSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)))):^20,}\
{(materiaprimaAmetros_inventarioFinalSegundoSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))-(materiaprimaAmetros_inventarioInicialPrimerSemestre):^20,}\
{((materiaprimaAmetros_inventarioFinalSegundoSemestre)+(((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))\
                            +((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))))-(materiaprimaAmetros_inventarioInicialPrimerSemestre):^20,}
{'Precio de compra':<30} ${materiaprimaAmetros_costoPrimerSemestre:^19,.1f} ${materiaprimaAmetros_costoSegundoSemestre:^19,.1f}
{'Total de Materia A en $':<30} ${(materiaprimaAmetros_costoPrimerSemestre)*((materiaprimaAmetros_inventarioInicialPrimerSemestre)-(materiaprimaAmetros_inventarioInicialPrimerSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))):^19,.2f}\
${(materiaprimaAmetros_costoSegundoSemestre)*((materiaprimaAmetros_inventarioFinalSegundoSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))-(materiaprimaAmetros_inventarioInicialPrimerSemestre)):^19,.2f}\
${((materiaprimaAmetros_costoPrimerSemestre)*((materiaprimaAmetros_inventarioInicialPrimerSemestre)-(materiaprimaAmetros_inventarioInicialPrimerSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))))+((materiaprimaAmetros_costoSegundoSemestre)*((materiaprimaAmetros_inventarioFinalSegundoSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))-(materiaprimaAmetros_inventarioInicialPrimerSemestre))):^19,.2f}
{'-' * 90}
Material B
{'Requerimiento de materiales':<30} {(materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))):^20,}\
 {(materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))):^20,}\
 {((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))\
                            +((materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))):^20,}
{'Inventario final':<30} {materiaprimaBmetros_inventarioInicialPrimerSemestre:^20,} {materiaprimaBmetros_inventarioFinalSegundoSemestre:^20,} {materiaprimaBmetros_inventarioFinalSegundoSemestre:^20,}
{'Total de materiales':<30} {(materiaprimaBmetros_inventarioInicialPrimerSemestre)+((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)))):^20,}\
 {(materiaprimaBmetros_inventarioFinalSegundoSemestre)+(materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))):^20,}\
{(((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))\
                            +((materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))))\
        +(materiaprimaBmetros_inventarioFinalSegundoSemestre):^20,}
{'Inventario inicial':<30} {materiaprimaBmetros_inventarioInicialPrimerSemestre:^20,} {materiaprimaBmetros_inventarioInicialPrimerSemestre:^20,} {materiaprimaBmetros_inventarioInicialPrimerSemestre:^20,}
{'Material a comprar':<30} {((materiaprimaBmetros_inventarioInicialPrimerSemestre)+((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)))))\
                            -(materiaprimaBmetros_inventarioInicialPrimerSemestre):^20,}\
 {(materiaprimaBmetros_inventarioFinalSegundoSemestre)+(materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))-(materiaprimaBmetros_inventarioInicialPrimerSemestre):^20,}\
{((((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))\
                            +((materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))))\
        +(materiaprimaBmetros_inventarioFinalSegundoSemestre))-(materiaprimaBmetros_inventarioInicialPrimerSemestre):^20,}
{'Precio de compra':<30} ${materiaprimaBmetros_costoPrimerSemestre:^19,.2f} ${materiaprimaBmetros_costoSegundoSemestre:^20,.2f}
{'Total de material B en $':<30} ${(materiaprimaBmetros_costoPrimerSemestre)*(((materiaprimaBmetros_inventarioInicialPrimerSemestre)+((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)))))\
                            -(materiaprimaBmetros_inventarioInicialPrimerSemestre)):^20,.2f}\
${(materiaprimaBmetros_costoSegundoSemestre)*((materiaprimaBmetros_inventarioFinalSegundoSemestre)+(materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))-(materiaprimaBmetros_inventarioInicialPrimerSemestre)):^19,.2f}\
${((materiaprimaBmetros_costoPrimerSemestre)*(((materiaprimaBmetros_inventarioInicialPrimerSemestre)+((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)))))\
                            -(materiaprimaBmetros_inventarioInicialPrimerSemestre)))+((materiaprimaBmetros_costoSegundoSemestre)*((materiaprimaBmetros_inventarioFinalSegundoSemestre)+(materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))-(materiaprimaBmetros_inventarioInicialPrimerSemestre))):^20,.2f}
{'-' * 90}
Material C
{'Requerimiento de materiales':<30} {(materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))):^20,}\
 {(materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))):^20,}\
 {((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))\
                            +((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))):^20,}
{'Inventario final':<30} {materiaprimaCpiezas_inventarioInicialPrimerSemestre:^20,} {materiaprimaCpiezas_inventarioFinalSegundoSemestre:^20,} {materiaprimaCpiezas_inventarioFinalSegundoSemestre:^20,} 
{'Total de materiales':<30} {((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioInicialPrimerSemestre):^20,} \
{((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioFinalSegundoSemestre):^20,} \
{(((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))\
                            +((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))))+(materiaprimaCpiezas_inventarioFinalSegundoSemestre):^20,}
{'Inventario inicial':<30} {materiaprimaCpiezas_inventarioInicialPrimerSemestre:^20,} {materiaprimaCpiezas_inventarioInicialPrimerSemestre:^20,} {materiaprimaCpiezas_inventarioInicialPrimerSemestre:^20,}
{'Material a comprar':<30} {(((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioInicialPrimerSemestre))\
                            -(materiaprimaCpiezas_inventarioInicialPrimerSemestre):^20,} \
{(((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioFinalSegundoSemestre))-(materiaprimaCpiezas_inventarioInicialPrimerSemestre):^20,} \
{((((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))\
                            +((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))))+(materiaprimaCpiezas_inventarioFinalSegundoSemestre))-(materiaprimaCpiezas_inventarioInicialPrimerSemestre):^20,}
{'Precio de compra':<30} ${materiaprimaCpiezas_costoPrimerSemestre:^19,.1f} ${materiaprimaCpiezas_costoSegundoSemestre:^19,.1f}
{'Total de material C en $':<30} ${(materiaprimaCpiezas_costoPrimerSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioInicialPrimerSemestre))\
                            -(materiaprimaCpiezas_inventarioInicialPrimerSemestre)):^19,.2f} \
${(materiaprimaCpiezas_costoSegundoSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioFinalSegundoSemestre))-(materiaprimaCpiezas_inventarioInicialPrimerSemestre)):^19,.2f} \
${((materiaprimaCpiezas_costoPrimerSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioInicialPrimerSemestre))\
                            -(materiaprimaCpiezas_inventarioInicialPrimerSemestre)))+((materiaprimaCpiezas_costoSegundoSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioFinalSegundoSemestre))-(materiaprimaCpiezas_inventarioInicialPrimerSemestre))):^19,.2f}
{'-' * 90}
{'Compras totales':<30} ${((materiaprimaAmetros_costoPrimerSemestre)*((materiaprimaAmetros_inventarioInicialPrimerSemestre)-(materiaprimaAmetros_inventarioInicialPrimerSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))))\
                            +((materiaprimaBmetros_costoPrimerSemestre)*(((materiaprimaBmetros_inventarioInicialPrimerSemestre)+((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)))))\
                            -(materiaprimaBmetros_inventarioInicialPrimerSemestre)))\
                                +((materiaprimaCpiezas_costoPrimerSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioInicialPrimerSemestre))\
                            -(materiaprimaCpiezas_inventarioInicialPrimerSemestre))):^19,.2f} \
${((materiaprimaAmetros_costoSegundoSemestre)*((materiaprimaAmetros_inventarioFinalSegundoSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))-(materiaprimaAmetros_inventarioInicialPrimerSemestre)))\
        +((materiaprimaBmetros_costoSegundoSemestre)*((materiaprimaBmetros_inventarioFinalSegundoSemestre)+(materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))-(materiaprimaBmetros_inventarioInicialPrimerSemestre)))\
        +((materiaprimaCpiezas_costoSegundoSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioFinalSegundoSemestre))-(materiaprimaCpiezas_inventarioInicialPrimerSemestre))):^19,.2f} \
${(((materiaprimaAmetros_costoPrimerSemestre)*((materiaprimaAmetros_inventarioInicialPrimerSemestre)-(materiaprimaAmetros_inventarioInicialPrimerSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))))+((materiaprimaAmetros_costoSegundoSemestre)*((materiaprimaAmetros_inventarioFinalSegundoSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))-(materiaprimaAmetros_inventarioInicialPrimerSemestre))))\
        +(((materiaprimaBmetros_costoPrimerSemestre)*(((materiaprimaBmetros_inventarioInicialPrimerSemestre)+((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)))))\
                            -(materiaprimaBmetros_inventarioInicialPrimerSemestre)))+((materiaprimaBmetros_costoSegundoSemestre)*((materiaprimaBmetros_inventarioFinalSegundoSemestre)+(materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))-(materiaprimaBmetros_inventarioInicialPrimerSemestre))))\
        +(((materiaprimaCpiezas_costoPrimerSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioInicialPrimerSemestre))\
                            -(materiaprimaCpiezas_inventarioInicialPrimerSemestre)))+((materiaprimaCpiezas_costoSegundoSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioFinalSegundoSemestre))-(materiaprimaCpiezas_inventarioInicialPrimerSemestre)))):^19,.2f}
{'-' * 90}
''')
    
def determinacion_saldo_proveedores_y_flujo_salidas():
    print(f'''
{'-' * 70}
{'DETERMINACION DEL SALDO DE PROVEEDORES Y EL FLUJO DE SALIDAS':^70}
{'-' * 70}
{'Descripcion':^30} {'Importe':^20} {'Total':^20}
{'-' * 70}
{'Salida de proveedores':<30} {'':^20} ${proveedores:^19,.2f}
{'Compras Año actual':<30} {'':^20} ${(((materiaprimaAmetros_costoPrimerSemestre)*((materiaprimaAmetros_inventarioInicialPrimerSemestre)-(materiaprimaAmetros_inventarioInicialPrimerSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))))+((materiaprimaAmetros_costoSegundoSemestre)*((materiaprimaAmetros_inventarioFinalSegundoSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))-(materiaprimaAmetros_inventarioInicialPrimerSemestre))))\
        +(((materiaprimaBmetros_costoPrimerSemestre)*(((materiaprimaBmetros_inventarioInicialPrimerSemestre)+((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)))))\
                            -(materiaprimaBmetros_inventarioInicialPrimerSemestre)))+((materiaprimaBmetros_costoSegundoSemestre)*((materiaprimaBmetros_inventarioFinalSegundoSemestre)+(materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))-(materiaprimaBmetros_inventarioInicialPrimerSemestre))))\
        +(((materiaprimaCpiezas_costoPrimerSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioInicialPrimerSemestre))\
                            -(materiaprimaCpiezas_inventarioInicialPrimerSemestre)))+((materiaprimaCpiezas_costoSegundoSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioFinalSegundoSemestre))-(materiaprimaCpiezas_inventarioInicialPrimerSemestre)))):^19,.2f}
{'Total de proveedores Año actual':<30} {'':^20}${(proveedores)+((((materiaprimaAmetros_costoPrimerSemestre)*((materiaprimaAmetros_inventarioInicialPrimerSemestre)-(materiaprimaAmetros_inventarioInicialPrimerSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))))+((materiaprimaAmetros_costoSegundoSemestre)*((materiaprimaAmetros_inventarioFinalSegundoSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))-(materiaprimaAmetros_inventarioInicialPrimerSemestre))))\
        +(((materiaprimaBmetros_costoPrimerSemestre)*(((materiaprimaBmetros_inventarioInicialPrimerSemestre)+((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)))))\
                            -(materiaprimaBmetros_inventarioInicialPrimerSemestre)))+((materiaprimaBmetros_costoSegundoSemestre)*((materiaprimaBmetros_inventarioFinalSegundoSemestre)+(materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))-(materiaprimaBmetros_inventarioInicialPrimerSemestre))))\
        +(((materiaprimaCpiezas_costoPrimerSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioInicialPrimerSemestre))\
                            -(materiaprimaCpiezas_inventarioInicialPrimerSemestre)))+((materiaprimaCpiezas_costoSegundoSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioFinalSegundoSemestre))-(materiaprimaCpiezas_inventarioInicialPrimerSemestre))))):^19,.2f}

Salidas de efectivo:
{'Por proveedores de año anterior':<30} ${(proveedores)*(proveedores2015_pago):^19,.2f}
{'Por proveedores del año actual':<30}  ${((((materiaprimaAmetros_costoPrimerSemestre)*((materiaprimaAmetros_inventarioInicialPrimerSemestre)-(materiaprimaAmetros_inventarioInicialPrimerSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))))+((materiaprimaAmetros_costoSegundoSemestre)*((materiaprimaAmetros_inventarioFinalSegundoSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))-(materiaprimaAmetros_inventarioInicialPrimerSemestre))))\
        +(((materiaprimaBmetros_costoPrimerSemestre)*(((materiaprimaBmetros_inventarioInicialPrimerSemestre)+((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)))))\
                            -(materiaprimaBmetros_inventarioInicialPrimerSemestre)))+((materiaprimaBmetros_costoSegundoSemestre)*((materiaprimaBmetros_inventarioFinalSegundoSemestre)+(materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))-(materiaprimaBmetros_inventarioInicialPrimerSemestre))))\
        +(((materiaprimaCpiezas_costoPrimerSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioInicialPrimerSemestre))\
                            -(materiaprimaCpiezas_inventarioInicialPrimerSemestre)))+((materiaprimaCpiezas_costoSegundoSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioFinalSegundoSemestre))-(materiaprimaCpiezas_inventarioInicialPrimerSemestre)))))*(comprasPresupuestadas_pago):^19,.2f}
{'Total de salidas año actual':<30} {'':^20} ${((proveedores)*(proveedores2015_pago))+(((((materiaprimaAmetros_costoPrimerSemestre)*((materiaprimaAmetros_inventarioInicialPrimerSemestre)-(materiaprimaAmetros_inventarioInicialPrimerSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))))+((materiaprimaAmetros_costoSegundoSemestre)*((materiaprimaAmetros_inventarioFinalSegundoSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))-(materiaprimaAmetros_inventarioInicialPrimerSemestre))))\
        +(((materiaprimaBmetros_costoPrimerSemestre)*(((materiaprimaBmetros_inventarioInicialPrimerSemestre)+((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)))))\
                            -(materiaprimaBmetros_inventarioInicialPrimerSemestre)))+((materiaprimaBmetros_costoSegundoSemestre)*((materiaprimaBmetros_inventarioFinalSegundoSemestre)+(materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))-(materiaprimaBmetros_inventarioInicialPrimerSemestre))))\
        +(((materiaprimaCpiezas_costoPrimerSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioInicialPrimerSemestre))\
                            -(materiaprimaCpiezas_inventarioInicialPrimerSemestre)))+((materiaprimaCpiezas_costoSegundoSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioFinalSegundoSemestre))-(materiaprimaCpiezas_inventarioInicialPrimerSemestre)))))*(comprasPresupuestadas_pago)):^19,.2f}
{'Saldo de proveedores año actual':<30} {'':^20}${((((materiaprimaAmetros_costoPrimerSemestre)*((materiaprimaAmetros_inventarioInicialPrimerSemestre)-(materiaprimaAmetros_inventarioInicialPrimerSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaAmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaAmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))))+((materiaprimaAmetros_costoSegundoSemestre)*((materiaprimaAmetros_inventarioFinalSegundoSemestre)+((materiaprimaAmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
+(materiaprimaAmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaAmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))-(materiaprimaAmetros_inventarioInicialPrimerSemestre))))\
        +(((materiaprimaBmetros_costoPrimerSemestre)*(((materiaprimaBmetros_inventarioInicialPrimerSemestre)+((materiaprimaBmetros_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaBmetros_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaBmetros_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre)))))\
                            -(materiaprimaBmetros_inventarioInicialPrimerSemestre)))+((materiaprimaBmetros_costoSegundoSemestre)*((materiaprimaBmetros_inventarioFinalSegundoSemestre)+(materiaprimaBmetros_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaBmetros_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaBmetros_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre)))-(materiaprimaBmetros_inventarioInicialPrimerSemestre))))\
        +(((materiaprimaCpiezas_costoPrimerSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
                    +(materiaprimaCpiezas_producto2*((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
                        +(materiaprimaCpiezas_producto3*((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioInicialPrimerSemestre))\
                            -(materiaprimaCpiezas_inventarioInicialPrimerSemestre)))+((materiaprimaCpiezas_costoSegundoSemestre)*((((materiaprimaCpiezas_producto1*((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre)))\
  +(materiaprimaCpiezas_producto2*((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre)))\
    +(materiaprimaCpiezas_producto3*((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre))))+(materiaprimaCpiezas_inventarioFinalSegundoSemestre))-(materiaprimaCpiezas_inventarioInicialPrimerSemestre)))))*(comprasPresupuestadas_pago):^19,.2f}
{'-' * 70}
''')

def presupuesto_mano_de_obra_directa():
    print(f'''
{'-' * 88}
{'PRESUPUESTO DE MANO DE OBRA DIRECTA':^88}
{'-' * 88}
{'':<30} {'1er. Semestre':^20} {'2do. Semestre':^20} {'Total 2009':^10}
{'-' * 88}
{'Producto CL':<30}
{'Unidades a producir':<30} {(ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-(producto1_inventarioInicialPrimerSemestre):^20,} {(ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-(producto1_inventarioInicialPrimerSemestre):^20,} {((ventasPlaneadasPrimerSemestre_producto1+ventasPlaneadasSegundoSemestre_producto1)+(producto1_inventarioFinalSegundoSemestre))-(producto1_inventarioInicialPrimerSemestre):^20,}
{'Horas requeridas por unidad':<30} {horasManoDeObra_producto1:^20} {horasManoDeObra_producto1:^20} {horasManoDeObra_producto1:^20}
{'Total de horas requeridas':<30} {((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-producto1_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto1):^20,} {((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-producto1_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto1):^20,} {(((ventasPlaneadasPrimerSemestre_producto1+ventasPlaneadasSegundoSemestre_producto1)+(producto1_inventarioFinalSegundoSemestre))-producto1_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto1):^20,}
{'Cuota por hora':<30} ${15.00:^20,.2f} ${18.00:^20,.2f} {'':^20}
{'Importe de M.O.D.':<30} ${((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-producto1_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto1) * 15.00:^20,.2f} ${((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-producto1_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto1) * 18.00:^20,.2f} ${(((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-producto1_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto1) * 15.00) + (((ventasPlaneadasSegundoSemestre_producto1 + producto1_inventarioFinalSegundoSemestre)-producto1_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto1) * 18.00):^20,.2f}
{'-' * 88}
{'Producto CE':<30}
{'Unidades a producir':<30} {(ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-(producto2_inventarioInicialPrimerSemestre):^20,} {(ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-(producto2_inventarioInicialPrimerSemestre):^20,} {((ventasPlaneadasPrimerSemestre_producto2+ventasPlaneadasSegundoSemestre_producto2)+(producto2_inventarioFinalSegundoSemestre))-(producto2_inventarioInicialPrimerSemestre):^20,}
{'Horas requeridas por unidad':<30} {horasManoDeObra_producto2:^20} {horasManoDeObra_producto2:^20} {horasManoDeObra_producto2:^20}
{'Total de horas requeridas':<30} {((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-producto2_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto2):^20,} {((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-producto2_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto2):^20,} {(((ventasPlaneadasPrimerSemestre_producto2+ventasPlaneadasSegundoSemestre_producto2)+(producto2_inventarioFinalSegundoSemestre))-producto2_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto2):^20,}
{'Cuota por hora':<30} ${15.00:^20,.2f} ${18.00:^20,.2f} {'':^20}
{'Importe de M.O.D.':<30} ${((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-producto2_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto2) * 15.00:^20,.2f} ${((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-producto2_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto2) * 18.00:^20,.2f} ${(((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-producto2_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto2) * 15.00) + (((ventasPlaneadasSegundoSemestre_producto2 + producto2_inventarioFinalSegundoSemestre)-producto2_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto2) * 18.00):^20,.2f}
{'-' * 88}
{'Producto CR':<30}
{'Unidades a producir':<30} {(ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-(producto3_inventarioInicialPrimerSemestre):^20,} {(ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-(producto3_inventarioInicialPrimerSemestre):^20,} {((ventasPlaneadasPrimerSemestre_producto3+ventasPlaneadasSegundoSemestre_producto3)+(producto3_inventarioFinalSegundoSemestre))-(producto3_inventarioInicialPrimerSemestre):^20,}
{'Horas requeridas por unidad':<30} {horasManoDeObra_producto3:^20} {horasManoDeObra_producto3:^20} {horasManoDeObra_producto3:^20}
{'Total de horas requeridas':<30} {((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-producto3_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto3):^20,} {((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-producto3_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto3):^20,} {(((ventasPlaneadasPrimerSemestre_producto3+ventasPlaneadasSegundoSemestre_producto3)+(producto3_inventarioFinalSegundoSemestre))-producto3_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto3):^20,}
{'Cuota por hora':<30} ${15.00:^20,.2f} ${18.00:^20,.2f} {'':^20}
{'Importe de M.O.D.':<30} ${((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-producto3_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto3) * 15.00:^20,.2f} ${((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-producto3_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto3) * 18.00:^20,.2f} ${(((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-producto3_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto3) * 15.00) + (((ventasPlaneadasSegundoSemestre_producto3 + producto3_inventarioFinalSegundoSemestre)-producto3_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto3) * 18.00):^20,.2f}
{'-' * 88}
{'Total de horas requeridas por semestre':<30} {((ventasPlaneadasPrimerSemestre_producto1 + producto1_inventarioInicialPrimerSemestre)-producto1_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto1) + ((ventasPlaneadasPrimerSemestre_producto2 + producto2_inventarioInicialPrimerSemestre)-producto2_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto2) + ((ventasPlaneadasPrimerSemestre_producto3 + producto3_inventarioInicialPrimerSemestre)-producto3_inventarioInicialPrimerSemestre) * (horasManoDeObra_producto3):^20,.2f} {13000 + 10800 + 11250:^20,.2f} {37000 + 24300 + 21750:^20,.2f}
{'Total de M.O.D. por semestre':<30} ${(24000 * 15.00) + (13500 * 15.00) + (10500 * 15.00):^20,.2f} ${(13000 * 18.00) + (10800 * 18.00) + (11250 * 18.00):^20,.2f} ${((24000 * 15.00) + (13500 * 15.00) + (10500 * 15.00)) + ((13000 * 18.00) + (10800 * 18.00) + (11250 * 18.00)):^20,.2f}
{'-' * 88}
''')

def presupuesto_gastos_indirectos_fabricacion():
    print(f'''
{'-' * 88}
{'PRESUPUESTO DE GASTOS INDIRECTOS DE FABRICACIÓN':^88}
{'-' * 88}
{'':<30} {'1er. Semestre':^20} {'2do. Semestre':^20} {'Total 2016':^10}
{'-' * 88}
{'Depreciación':<30} ${deprecioacion_GIF/2:^20,.2f} ${deprecioacion_GIF/2:^20,.2f} ${deprecioacion_GIF:^20,.2f}
{'Seguros':<30} ${seguros_GIF/2:^20,.2f} ${seguros_GIF/2:^20,.2f} ${seguros_GIF:^20,.2f}
{'Mantenimiento':<30} ${mantenimientoPrimerSemestre_GIF:^20,.2f} ${mantenimientoSegundoSemestre_GIF:^20,.2f} ${mantenimientoPrimerSemestre_GIF + mantenimientoSegundoSemestre_GIF:^20,.2f}
{'Energéticos':<30} ${energeticosPrimerSemestre_GIF:^20,.2f} ${energeticosSegundoSemestre_GIF:^20,.2f} ${energeticosPrimerSemestre_GIF + energeticosSegundoSemestre_GIF:^20,.2f}
{'Varios':<30} ${varios_GIF/2:^20,.2f} ${varios_GIF/2:^20,.2f} ${varios_GIF:^20,.2f}
{'-' * 88}
{'Total G.I.F. por semestre':<30} ${deprecioacion_GIF/2+seguros_GIF/2+mantenimientoPrimerSemestre_GIF+energeticosPrimerSemestre_GIF+varios_GIF/2:^20,.2f} ${deprecioacion_GIF/2+seguros_GIF/2+mantenimientoSegundoSemestre_GIF+energeticosSegundoSemestre_GIF+varios_GIF/2:^20,.2f} ${deprecioacion_GIF/2+seguros_GIF/2+mantenimientoPrimerSemestre_GIF+energeticosPrimerSemestre_GIF+varios_GIF/2 + deprecioacion_GIF/2+seguros_GIF/2+mantenimientoSegundoSemestre_GIF+energeticosSegundoSemestre_GIF+varios_GIF/2:^20,.2f}
{'-' * 88}
{'Coeficiente para determinar el costo por hora de Gastos Indirectos de Fabricación':<88}
{'Total de G.I.F.':<30} {'':<20} {'':<20} ${deprecioacion_GIF/2+seguros_GIF/2+mantenimientoPrimerSemestre_GIF+energeticosPrimerSemestre_GIF+varios_GIF/2 + deprecioacion_GIF/2+seguros_GIF/2+mantenimientoSegundoSemestre_GIF+energeticosSegundoSemestre_GIF+varios_GIF/2:^20,.2f}
{'Total horas M.O.D. Anual':<30} {'':<20} {'':<20} {(37000 + 24300 + 21750):^20,.2f}
{'Costo por Hora de G.I.F.':<30} {'':<20} {'':<20} ${(deprecioacion_GIF/2+seguros_GIF/2+mantenimientoPrimerSemestre_GIF+energeticosPrimerSemestre_GIF+varios_GIF/2 + deprecioacion_GIF/2+seguros_GIF/2+mantenimientoSegundoSemestre_GIF+energeticosSegundoSemestre_GIF+varios_GIF/2) / (37000 + 24300 + 21750):^20,.2f}
{'-' * 88}
''')

def presupuesto_gastos_operacion():
    print(f'''
{'-' * 88}
{'PRESUPUESTO DE GASTOS DE OPERACIÓN':^88}
{'-' * 88}
{'':<30} {'1er. Semestre':^20} {'2do. Semestre':^20} {'Total 2016':^10}
{'-' * 88}
{'Depreciación':<30} ${7500:^20,.2f} ${7500:^20,.2f} ${7500 + 7500:^20,.2f}
{'Sueldos y Salarios':<30} ${125000:^20,.2f} ${125000:^20,.2f} ${125000 + 125000:^20,.2f}
{'Comisiones':<30} ${86750:^20,.2f} ${85580:^20,.2f} ${86750 + 85580:^20,.2f}
{'Varios':<30} ${10000:^20,.2f} ${8000:^20,.2f} ${10000 + 8000:^20,.2f}
{'Intereses del Préstamo':<30} ${2500:^20,.2f} ${2500:^20,.2f} ${2500 + 2500:^20,.2f}
{'-' * 88}
{'Total de Gastos de Operación':<30} ${231750:^20,.2f} ${228580:^20,.2f} ${231750 + 228580:^20,.2f}
{'-' * 88}
''')


def determinacion_costo_unitario():
    print(f'''
{'-' * 88}
{'DETERMINACIÓN DEL COSTO UNITARIO DE PRODUCTOS TERMINADOS':^88}
{'-' * 88}
{'Descripción':<30} {'PRODUCTO CL':^50}
{'':<30} {'Costo':^10} {'Cantidad':^10} {'Costo Unitario':^10}
{'-' * 88}
{'Material A':<30} ${12.00:^10,.2f} {1.0:^10} ${12.00:^10,.2f}
{'Material B':<30} ${3.00:^10,.2f} {0.5:^10} ${1.50:^10,.2f}
{'Material C':<30} ${2.00:^10,.2f} {10.0:^10} ${20.00:^10,.2f}
{'Mano de Obra':<30} ${18.00:^10,.2f} {2.0:^10} ${36.00:^10,.2f}
{'Gastos Indirectos de Fabricación':<30} ${3.17:^10,.2f} {2.0:^10} ${6.33:^10,.2f}
{'-' * 88}
{'Costo Unitario':<30} {'':^30} ${75.83:^10,.2f}

{'-' * 88}
{'Descripción':<30} {'PRODUCTO CE':^50}
{'':<30} {'Costo':^10} {'Cantidad':^10} {'Costo Unitario':^10}
{'-' * 88}
{'Material A':<30} ${12.00:^10,.2f} {1.2:^10} ${14.40:^10,.2f}
{'Material B':<30} ${3.00:^10,.2f} {0.6:^10} ${1.80:^10,.2f}
{'Material C':<30} ${2.00:^10,.2f} {25.0:^10} ${50.00:^10,.2f}
{'Mano de Obra':<30} ${18.00:^10,.2f} {1.0:^10} ${18.00:^10,.2f}
{'Gastos Indirectos de Fabricación':<30} ${3.17:^10,.2f} {1.0:^10} ${3.17:^10,.2f}
{'-' * 88}
{'Costo Unitario':<30} {'':^30} ${87.37:^10,.2f}

{'-' * 88}
{'Descripción':<30} {'PRODUCTO CR':^50}
{'':<30} {'Costo':^10} {'Cantidad':^10} {'Costo Unitario':^10}
{'-' * 88}
{'Material A':<30} ${12.00:^10,.2f} {2.0:^10} ${24.00:^10,.2f}
{'Material B':<30} ${3.00:^10,.2f} {1.0:^10} ${3.00:^10,.2f}
{'Material C':<30} ${2.00:^10,.2f} {5.0:^10} ${10.00:^10,.2f}
{'Mano de Obra':<30} ${18.00:^10,.2f} {1.5:^10} ${27.00:^10,.2f}
{'Gastos Indirectos de Fabricación':<30} ${3.17:^10,.2f} {1.5:^10} ${4.76:^10,.2f}
{'-' * 88}
{'Costo Unitario':<30} {'':^30} ${68.76:^10,.2f}
{'-' * 88}
''')

def valuacion_inventarios_finales():
    print(f'''
{'-' * 88}
{'VALUACIÓN DE INVENTARIOS FINALES':^88}
{'-' * 88}

{'INVENTARIO FINAL DE MATERIALES':^88}
{'Descripción':<30} {'Unidades':^10} {'Costo Unitario':^20} {'Costo Total':^20}
{'-' * 88}
{'Material A':<30} {3000:^10} ${12.00:^20,.2f} ${3000 * 12.00:^20,.2f}
{'Material B':<30} {2500:^10} ${3.00:^20,.2f} ${2500 * 3.00:^20,.2f}
{'Material C':<30} {1800:^10} ${2.00:^20,.2f} ${1800 * 2.00:^20,.2f}
{'-' * 88}
{'Inventario Final de Materiales':<30} {'':<10} {'':<20} ${3000 * 12.00 + 2500 * 3.00 + 1800 * 2.00:^20,.2f}

{'-' * 88}

{'INVENTARIO FINAL DE PRODUCTO TERMINADO':^88}
{'Descripción':<30} {'Unidades':^10} {'Costo Unitario':^20} {'Costo Total':^20}
{'-' * 88}
{'Producto CL':<30} {6500:^10} ${75.83:^20,.2f} ${6500 * 75.83:^20,.2f}
{'Producto CE':<30} {7500:^10} ${87.37:^20,.2f} ${7500 * 87.37:^20,.2f}
{'Producto CR':<30} {5000:^10} ${68.76:^20,.2f} ${5000 * 68.76:^20,.2f}
{'-' * 88}
{'Inventario Final de Producto Terminado':<30} {'':<10} {'':<20} ${6500 * 75.83 + 7500 * 87.37 + 5000 * 68.76:^20,.2f}
{'-' * 88}
''')





def estado_costo_produccion_ventas():
    
    saldo_inicial_materiales = 45000
    compras_materiales = 2141010
    inventario_final_materiales = 47100
    mano_obra_directa = 1350900
    gastos_fabricacion_indirectos = 263000
    inventario_inicial_productos_terminados = 135000
    inventario_final_productos_terminados = 1491968
    
   
    material_disponible = saldo_inicial_materiales + compras_materiales
    materiales_utilizados = material_disponible - inventario_final_materiales
    costo_produccion = materiales_utilizados + mano_obra_directa + gastos_fabricacion_indirectos
    total_produccion_disponible = costo_produccion + inventario_inicial_productos_terminados
    costo_ventas = total_produccion_disponible - inventario_final_productos_terminados

    
    print(f'''
{'-' * 88}
{'ESTADO DE COSTO DE PRODUCCIÓN Y VENTAS':^88}
{'Presupuesto del 1 de Enero al 31 de Diciembre del 2016':^88}
{'-' * 88}

{'Saldo Inicial de Materiales':<60} ${saldo_inicial_materiales:>20,.2f}
{'(+) Compras de Materiales':<60} ${compras_materiales:>20,.2f}
{'=' * 88}
{'Material Disponible':<60} ${material_disponible:>20,.2f}
{'(-) Inventario Final de Materiales':<60} ${inventario_final_materiales:>20,.2f}
{'=' * 88}
{'Materiales Utilizados':<60} ${materiales_utilizados:>20,.2f}
{'(+) Mano de Obra Directa':<60} ${mano_obra_directa:>20,.2f}
{'(+) Gastos de Fabricación Indirectos':<60} ${gastos_fabricacion_indirectos:>20,.2f}
{'=' * 88}
{'Costo de Producción':<60} ${costo_produccion:>20,.2f}
{'(+) Inventario Inicial de Productos Terminados':<60} ${inventario_inicial_productos_terminados:>20,.2f}
{'=' * 88}
{'Total de Producción Disponible':<60} ${total_produccion_disponible:>20,.2f}
{'(-) Inventario Final de Productos Terminados':<60} ${inventario_final_productos_terminados:>20,.2f}
{'=' * 88}
{'Costo de Ventas':<60} ${costo_ventas:>20,.2f}
{'-' * 88}
''')


def estado_resultados():
    
    ventas = 17233000
    costo_ventas = 2395842
    gastos_operacion = 460330
    isr = 4313048
    ptu = 1437683

   
    utilidad_bruta = ventas - costo_ventas
    utilidad_operacion = utilidad_bruta - gastos_operacion
    utilidad_neta = utilidad_operacion - isr - ptu

    
    print(f'''
{'-' * 88}
{'ESTADO DE RESULTADOS':^88}
{'Presupuesto del 1 de Enero al 31 de Diciembre del 2016':^88}
{'-' * 88}

{'Ventas':<60} ${ventas:>20,.2f}
{'(-) Costo de Ventas':<60} ${costo_ventas:>20,.2f}
{'=' * 88}
{'Utilidad Bruta':<60} ${utilidad_bruta:>20,.2f}
{'(-) Gastos de Operación':<60} ${gastos_operacion:>20,.2f}
{'=' * 88}
{'Utilidad de Operación':<60} ${utilidad_operacion:>20,.2f}
{'(-) ISR':<60} ${isr:>20,.2f}
{'(-) PTU':<60} ${ptu:>20,.2f}
{'=' * 88}
{'Utilidad Neta':<60} ${utilidad_neta:>20,.2f}
{'-' * 88}
''')


def estado_flujo_efectivo():
    
    saldo_inicial_efectivo = 100000
    cobranza_2016 = 13786400
    cobranza_2015 = 80000
    proveedores_2016 = 1070505
    proveedores_2015 = 33500
    pago_mano_obra_directa = 1350900
    pago_gastos_indirectos_fabricacion = 183000
    pago_gastos_operacion = 445330
    compra_activo_fijo = 85000
    pago_isr_2015 = 50000
    pago_isr_2016 = 0

    
    total_entradas = cobranza_2016 + cobranza_2015
    efectivo_disponible = saldo_inicial_efectivo + total_entradas
    total_salidas = (proveedores_2016 + proveedores_2015 + pago_mano_obra_directa +
                     pago_gastos_indirectos_fabricacion + pago_gastos_operacion +
                     compra_activo_fijo + pago_isr_2015 + pago_isr_2016)
    flujo_efectivo_actual = efectivo_disponible - total_salidas

    
    print(f'''
{'-' * 88}
{'ESTADO DE FLUJO DE EFECTIVO':^88}
{'Presupuesto del 1 de Enero al 31 de Diciembre del 2016':^88}
{'-' * 88}

{'Saldo Inicial de Efectivo':<60} ${saldo_inicial_efectivo:>20,.2f}

{'Entradas:':^88}
{'Cobranza 2016':<60} ${cobranza_2016:>20,.2f}
{'Cobranza 2015':<60} ${cobranza_2015:>20,.2f}
{'=' * 88}
{'Total de Entradas':<60} ${total_entradas:>20,.2f}
{'Efectivo Disponible':<60} ${efectivo_disponible:>20,.2f}

{'Salidas:':^88}
{'Proveedores 2016':<60} ${proveedores_2016:>20,.2f}
{'Proveedores 2015':<60} ${proveedores_2015:>20,.2f}
{'Pago Mano de Obra Directa':<60} ${pago_mano_obra_directa:>20,.2f}
{'Pago Gastos Indirectos de Fabricación':<60} ${pago_gastos_indirectos_fabricacion:>20,.2f}
{'Pago de Gastos de Operación':<60} ${pago_gastos_operacion:>20,.2f}
{'Compra de Activo Fijo (Maquinaria)':<60} ${compra_activo_fijo:>20,.2f}
{'Pago ISR 2015':<60} ${pago_isr_2015:>20,.2f}
{'Pago ISR 2016':<60} ${pago_isr_2016:>20,.2f}
{'=' * 88}
{'Total de Salidas':<60} ${total_salidas:>20,.2f}

{'Flujo de Efectivo Actual':<60} ${flujo_efectivo_actual:>20,.2f}
{'-' * 88}
''')



def balance_general():
    # Datos de activos
    efectivo = 10748165
    clientes = 3446600
    deudores_diversos = 35000
    funcionarios_y_empleados = 10500
    inventario_materiales = 47100
    inventario_producto_terminado = 1491968
    
    total_activos_circulantes = (efectivo + clientes + deudores_diversos +
                                 funcionarios_y_empleados + inventario_materiales +
                                 inventario_producto_terminado)

    terreno = 905000
    planta_y_equipo = 1585000
    depreciacion_acumulada = -745000

    total_activos_no_circulante = (terreno + planta_y_equipo + depreciacion_acumulada)
    total_activo = total_activos_circulantes + total_activos_no_circulante

    # Datos de pasivo
    proveedores = 1070505
    documentos_por_pagar = 95000
    isr_por_pagar = 4313048
    ptu_por_pagar = 1437683
    
    total_pasivo_corto_plazo = (proveedores + documentos_por_pagar + isr_por_pagar + ptu_por_pagar)

    prestamos_bancarios = 120000
    total_pasivo_largo_plazo = prestamos_bancarios
    total_pasivo = total_pasivo_corto_plazo + total_pasivo_largo_plazo

    # Datos de capital contable
    capital_aportado = 1500000
    capital_ganado = 362000
    utilidad_del_ejercicio = 8626097
    total_capital_contable = capital_aportado + capital_ganado + utilidad_del_ejercicio

    # Formato de salida
    print(f'''
{'-' * 88}
{'BALANCE GENERAL':^88}
{'Presupuesto al 31 de Diciembre del 2016':^88}
{'-' * 88}

{'ACTIVO':^88}
{'CIRCULANTE':^88}
{'Efectivo':<60} ${efectivo:>20,.2f}
{'Clientes':<60} ${clientes:>20,.2f}
{'Deudores Diversos':<60} ${deudores_diversos:>20,.2f}
{'Funcionarios y Empleados':<60} ${funcionarios_y_empleados:>20,.2f}
{'Inventario de Materiales':<60} ${inventario_materiales:>20,.2f}
{'Inventario de Producto Terminado':<60} ${inventario_producto_terminado:>20,.2f}
{'=' * 88}
{'Total de Activos Circulantes':<60} ${total_activos_circulantes:>20,.2f}

{'NO CIRCULANTE':^88}
{'Terreno':<60} ${terreno:>20,.2f}
{'Planta y Equipo':<60} ${planta_y_equipo:>20,.2f}
{'Depreciación Acumulada':<60} ${depreciacion_acumulada:>20,.2f}
{'=' * 88}
{'Total Activos No Circulante':<60} ${total_activos_no_circulante:>20,.2f}

{'ACTIVO TOTAL':<60} ${total_activo:>20,.2f}

{'PASIVO':^88}
{'CORTO PLAZO':^88}
{'Proveedores':<60} ${proveedores:>20,.2f}
{'Documentos por Pagar':<60} ${documentos_por_pagar:>20,.2f}
{'ISR por Pagar':<60} ${isr_por_pagar:>20,.2f}
{'PTU por Pagar':<60} ${ptu_por_pagar:>20,.2f}
{'=' * 88}
{'Total de Pasivo Corto Plazo':<60} ${total_pasivo_corto_plazo:>20,.2f}

{'LARGO PLAZO':^88}
{'Préstamos Bancarios':<60} ${prestamos_bancarios:>20,.2f}
{'=' * 88}
{'Total de Pasivo Largo Plazo':<60} ${total_pasivo_largo_plazo:>20,.2f}

{'PASIVO TOTAL':<60} ${total_pasivo:>20,.2f}

{'CAPITAL CONTABLE':^88}
{'Capital Aportado':<60} ${capital_aportado:>20,.2f}
{'Capital Ganado':<60} ${capital_ganado:>20,.2f}
{'Utilidad del Ejercicio':<60} ${utilidad_del_ejercicio:>20,.2f}
{'=' * 88}
{'Total de Capital Contable':<60} ${total_capital_contable:>20,.2f}

{'SUMA DE PASIVO Y CAPITAL':<60} ${total_pasivo + total_capital_contable:>20,.2f}
{'-' * 88}
''')









efectivo = 100000
clientes = 80000
deudores_diversos = 35000
funcionarios_y_empleados = 10500
inventario_materiales = 45000
inverntario_producto_terminado = 135000
total_activo_circulante = efectivo + clientes + deudores_diversos + funcionarios_y_empleados + inventario_materiales + inverntario_producto_terminado
terreno = 905000
planta_equipo = 1500000
depreciacion_acumulada = 650000
total_activo_no_circulante = terreno + planta_equipo + depreciacion_acumulada
activo_total = total_activo_circulante + total_activo_no_circulante
proveedores = 33500
documentos_por_pagar = 95000
isr_por_pagar = 5000
total_pasivos_corto_plazo = proveedores + documentos_por_pagar + isr_por_pagar
prestamos_bancarios = 120000
total_pasivo_largo_plazo = prestamos_bancarios
pasivo_total = total_pasivos_corto_plazo + total_pasivo_largo_plazo
capital_contribuido = 1500000
capital_ganado = 362000
capital_contable_total = capital_contribuido + capital_ganado
suma_pasivo_y_capital = pasivo_total + capital_contable_total

#REQUERIMIENTO DE MATERIALES
materiaprimaAmetros_producto1 = 1
materiaprimaAmetros_producto2 = 1.2 
materiaprimaAmetros_producto3 = 2

materiaprimaBmetros_producto1 = 0.5
materiaprimaBmetros_producto2 = 0.6
materiaprimaBmetros_producto3 = 1

materiaprimaCpiezas_producto1 = 10
materiaprimaCpiezas_producto2 = 25
materiaprimaCpiezas_producto3 = 5

horasManoDeObra_producto1 = 2
horasManoDeObra_producto2 = 1
horasManoDeObra_producto3 = 1.5

manoDeObraDirecta_primerSemestre = 15
manoDeObraDirecta_segundoSemestre = 18

#INFORMACION DE INVENTARIOS
materiaprimaAmetros_inventarioInicialPrimerSemestre =  5000
materiaprimaBmetros_inventarioInicialPrimerSemestre = 3000
materiaprimaCpiezas_inventarioInicialPrimerSemestre = 2000
producto1_inventarioInicialPrimerSemestre = 10000
producto2_inventarioInicialPrimerSemestre = 8500
producto3_inventarioInicialPrimerSemestre = 6000

materiaprimaAmetros_inventarioFinalSegundoSemestre = 3000
materiaprimaBmetros_inventarioFinalSegundoSemestre = 2500
materiaprimaCpiezas_inventarioFinalSegundoSemestre = 1800
producto1_inventarioFinalSegundoSemestre = 6500
producto2_inventarioFinalSegundoSemestre = 7500
producto3_inventarioFinalSegundoSemestre = 5000

materiaprimaAmetros_costoPrimerSemestre = 10
materiaprimaBmetros_costoPrimerSemestre = 2
materiaprimaCpiezas_costoPrimerSemestre = 1

materiaprimaAmetros_costoSegundoSemestre = 12
materiaprimaBmetros_costoSegundoSemestre = 3
materiaprimaCpiezas_costoSegundoSemestre = 2

#PRODUCTOS
precioVentasPrimerSemestre_producto1 = 300
precioVentasPrimerSemestre_producto2 = 280
precioVentasPrimerSemestre_producto3 = 185

precioVentasSegundoSemestre_producto1 = 320
precioVentasSegundoSemestre_producto2 = 310
precioVentasSegundoSemestre_producto3 = 200

ventasPlaneadasPrimerSemestre_producto1 = 12000
ventasPlaneadasPrimerSemestre_producto2 = 13500
ventasPlaneadasPrimerSemestre_producto3 = 7000

ventasPlaneadasSegundoSemestre_producto1 = 10000
ventasPlaneadasSegundoSemestre_producto2 = 11800
ventasPlaneadasSegundoSemestre_producto3 = 8500

#GASTOS DE ADMINISTRACION Y VENTAS
depreciacion_GAV = 15000
sueldos_salarios_GAV = 250000
comisiones_GAV = 1.01
variosPrimerSemestre_GAV = 10000
variosSegundoSemestre_GAV = 8000
interesesPorPrestamo_GAV = 5000

#GASTOS DE FABRICACION INDIRECTOS
deprecioacion_GIF = 80000
seguros_GIF = 25000
mantenimientoPrimerSemestre_GIF = 33000
mantenimientoSegundoSemestre_GIF = 25000
energeticosPrimerSemestre_GIF = 40000
energeticosSegundoSemestre_GIF = 35000
varios_GIF = 25000

#DATOS ADICIONALES

nuevoEquipo2016 = 85000
tasa_isr = 0.30
tasa_PTU = 0.10
saldoClientes2016_cobro = 1
ventasPresupuestadas_cobro = 0.8
proveedores2015_pago = 1
comprasPresupuestadas_pago = 0.5


presupuesto_ventas()
determinacion_saldo_de_clientes_flujo_de_entradas()
presupuesto_de_produccion()
presupuesto_de_requerimiento_de_materiales()
presupuesto_compra_materiales()
determinacion_saldo_proveedores_y_flujo_salidas()
presupuesto_mano_de_obra_directa()
presupuesto_gastos_indirectos_fabricacion()
presupuesto_gastos_operacion()
determinacion_costo_unitario()
valuacion_inventarios_finales()
estado_costo_produccion_ventas()
estado_resultados()
estado_flujo_efectivo()
balance_general()