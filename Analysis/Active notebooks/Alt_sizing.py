import math as m
import numpy as np

# physical constants
g_0 = 9.81                                           # gravitational acceleration [m/s/s]
R = 8.3145                                           # Universal gas constant [Pa*m^3/K*mol]

# Propellant properties
lox = {'M': 31.999 / 1000,                           # Molar mass [kg/mol]
       'T_e': 90.2,                                  # Propellant temperature [K]
       'C_pl': 1.70 * 1000,                          # Liquid phase specific heat [J/kg*K]
       'C_pv': 0.91 * 1000,                          # Vapor phase specific heat (constant pressure) [J/kg*K]
       'h_v': 213.05 * 1000,                         # Heat of vaporization [J/kg]
       'T_v': 90.2,                                  # Vaporization temperature [K]
       'R_p': R / (31.999 / 1000),                   # Specific gas constant
       'p_t': (350+70) * 1.1 * 6894,                 # Propellant tank initial pressure [Pa]
       'a': 1.382 / 10,                              # van der Wall constant A [Pa*m^6/mol^2]
       'b': 0.03186 / 1000,                          # van der Wall constant B [m^3/mol]
       'rho': 1141,                                  # Density [kg/m^3]
       'p_v': 101.4E3,                               # Operating point vapor pressure [Pa]
       'name': 'lox'
       }

ipa = {'M': 60.1 / 1000,                             # Molar mass [kg/mol]
       'T_e': 293,                                   # Propellant temperature [K]
       'C_pl': 435.725,                              # Liquid phase specific heat [J/kg*K]
       'C_pv': 1750,                                 # Vapor phase specific heat (constant pressure) [J/kg*K]
       'h_v': 2211.68,                               # Heat of vaporization [J/kg]
       'T_v': 355.8,                                 # Vaporization temperature [K]
       'R_p': R / (60.1 / 1000),                     # Specific gas constant
       'p_t': ((350                                  # Chamber pressure [psi]
             + 145                                   # Regen pressure drop [psi]
             + 70)                                   # Injector pressure drop [psi]
             * 1.1 * 6894),                          # Propellant tank initial pressure [Pa]
       'a': 12.18 / 10,                              # van der Wall constant A [Pa*m^6/mol^2]
       'b': 0.08407 / 1000,                          # van der Wall constant B [m^3/mol]
       'rho': 789,                                   # Density [kg/m^3]
       'p_v': 8.84E3,                                # Operating point vapor pressure [Pa]
       'name': 'ipa'
       }

# rocket model (assuming sea-level operation)
isp = 246 * 0.90                                     # specific impulse (sea-level, optimistic estimate) [s]
f = 3.2E3                                            # thrust [N]
mdot_t = f/(g_0 * isp)                               # total mass flowrate [kg/s]
chamber_p = 350 * 6.895 * 1000                       # chamber pressure (assumed to be 380 psi currently) [Pa]
loss_factor = 1.15                                   # estimate of line and injector losses
OF = 1.43                                            # mixture ratio 1.3 (erin) 1.43 optimum ******
mdot_o = mdot_t / (1 + (1/OF))                       # oxidizer mass flowrate [kg/s] ***
mdot_f = mdot_t / (1 + OF)                           # fuel mass flowrate [kg/s] ***
p_i = 101.3E3*2                                      # inlet pressure (currently 1 atm (gauge)) [Pa]
delta_p = chamber_p * loss_factor - p_i              # required pump discharge pressure [Pa]

# barleycorn conversions
g_0 = 32.2
delta_p *= 0.000145038                                 # [psi]

# def imperial_units(prop):
#     rho = prop['rho'] * 0.062428                     # [lb/ft^3]
#     h_v = prop['p_v'] * 0.000145038 * 144 / rho
#     if prop == ipa:
#         mdot = mdot_f * 2.20462                      # [lb/s]
#     elif prop == lox:
#         mdot = mdot_o * 2.20462                      # [lb/s]
#     q = mdot / rho                                   # volumetric flowrate [f^3/s]
#     h_p = 144 * delta_p / rho                        # required head rise [ft]
#     h_i = p_i * 0.000145038 * 144 / rho              # inlet head [ft]
#     npsh_a = h_i - h_v                               # Net Positive Suction Head (available) [ft]
#     return rho, h_v, mdot, q, h_p, npsh_a

# def print_results():
#     print("mass flow rate")
#     print("%.3f" % imperial_units(ipa)[2], "lbm/s (IPA)")
#     print("%.3f" % imperial_units(lox)[2], "lbm/s (LOX)", "\n")
#     print("volumetric flow rate")
#     print("%.4f" % imperial_units(ipa)[3], "ft^3/s (IPA)")
#     print("%.4f" % imperial_units(lox)[3], "ft^3/s (LOX)", "\n")
#     print("required pressure head")
#     print("%.3f" % imperial_units(ipa)[4], "ft (IPA)")
#     print("%.3f" % imperial_units(lox)[4], "ft (LOX)", "\n")
#     print("Net Positive Suction Head Available")
#     print("%.3f" % imperial_units(ipa)[5], "ft (IPA)")
#     print("%.3f" % imperial_units(lox)[5], "ft (LOX)", "\n")
# print_results()


def method_one(prop, N_r):
    rho = prop['rho'] * 0.062428                     # [lb/ft^3]
    omega_1 = (2 * m.pi * N_r) / 60                  # Angular velocity [rad/s]
    if prop == ipa:
        mdot = mdot_f * 2.20462                      # [lb/ft^3]
    elif prop == lox:
        mdot = mdot_o * 2.20462
    q = mdot / rho                                   # volumetric flowrate [f^3/s]
    h_p = (delta_p * 144) * (1 / (rho * g_0))        # required head rise [ft] ******

    return omega_1, q, h_p


print("volumetric flow rate")
print("%.4f" % method_one(lox, 30000)[1], "ft^3/s (LOX)", "\n")
print("required pressure head")
print("%.3f" % method_one(lox, 30000)[2], "ft (LOX)", "\n")



