# ==============================================================================
# Proyecto MISIÓN ESPACIAL: RESCATE EN MARTE
# Universidad del Caribe - Ingeniería en Datos e Inteligencia Organizacional
# ==============================================================================
import random

# ------------------------------------------------------------------------------
# COMPONENTE 2: Generación y selección de la tripulación
# RESPONSABLE: Valeria
# ------------------------------------------------------------------------------

def seleccionar_tripulacion():
    # Aquí se programa los 3 sorteos (S/N) con el random
    # Debe devolver la lista de tripulantes y el porcentaje de bonificación de 0 a 30
    tripulacion = ["Junior", "Junior", "Junior"] # Valor temporal de prueba
    bonificacion = 0
    return tripulacion, bonificacion

# ------------------------------------------------------------------------------
# COMPONENTE 3: Administración y consumo de recursos
# RESPONSABLE: Saúl
# ------------------------------------------------------------------------------

def consumir_recursos(comb, oxi, ener, c_base, o_base, e_base, bonificacion):
    # Aquí se calcula el consumo real con la fórmula base * (1 - bonificacion / 100)
    # Resta los recursos y devuelve los nuevos valores sin bajar de 0
    return comb, oxi, ener

# ------------------------------------------------------------------------------
# COMPONENTE 4: Generación de eventos aleatorios (Tormenta, Meteorito, Agujero o Nada)
# RESPONSABLE: Santiago
# ------------------------------------------------------------------------------

def evento_aleatorio(comb, oxi, ener, agujero_ocurrido):
    # Aquí se sortea el evento (excluyendo agujero negro si ya ocurrió en la ida)
    # Aplica las restas fijas y devuelve los recursos actualizados + si hubo falla mecánica
    es_falla_mecanica = False
    return comb, oxi, ener, es_falla_mecanica, agujero_ocurrido

# ------------------------------------------------------------------------------
# COMPONENTE 5: Falla mecánica (60%) y Estación de reabastecimiento
# RESPONSABLE: Izma
# ------------------------------------------------------------------------------

def aplicar_falla_mecanica(comb, oxi, ener):
    # Aquí se descuenta el 60% de cada recurso disponible y queda el 40%
    return comb, oxi, ener

def estacion_reabastecimiento(comb, oxi, ener):
    # Aquí se suma combustible (10, 20 o 30), oxígeno (1-20) y energía (1-25) sin pasar de 100
    return comb, oxi, ener

# ------------------------------------------------------------------------------
# COMPONENTE 6: Verificación de supervivencia (Victoria o Derrota)
# RESPONSABLE: Hector
# ------------------------------------------------------------------------------

def verificar_supervivencia(comb, oxi, ener, c_req, o_req, e_req):
    # Aquí se revisa si hay recursos suficientes para la siguiente acción
    # Devuelve True si sigue vivo, o False si perdió (imprimiendo la causa)
    return True

# ------------------------------------------------------------------------------
# COMPONENTE 1: Control general de la partida y Etapas 1 a 4
# RESPONSABLE: Erik
# ------------------------------------------------------------------------------

def iniciar_mision():
    print("=== MISION ESPACIAL: RESCATE EN MARTE ===")
    # Se inician los recursos
    combustible = 100.0
    oxigeno = 100.0
    energia = 100.0
