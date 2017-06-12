import math as m
from tabulate import tabulate

# Physical constants
g_0 = 9.81                                           # gravitational acceleration [m/s/s]
R = 8.3145                                           # Universal gas constant [Pa*m^3/K*mol]

# Propellant properties
lox = {'M': 31.999 / 1000,                           # Molar mass [kg/mol]
       'T_e': 90.2,                                  # Propellant temperature [K]
       'C_pl': 1.729 * 1000,                         # Liquid phase specific heat [J/kg*K]
       'C_pv': 0.919 * 1000,                         # Vapor phase specific heat (constant pressure) [J/kg*K]
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
       'C_pl': 7.25 * 1000 * (60.1 / 1000),          # Liquid phase specific heat [J/kg*K]
       'C_pv': 1.75 * 1000,                          # Vapor phase specific heat (constant pressure) [J/kg*K]
       'h_v': 36800 * (60.1 / 1000),                 # Heat of vaporization [J/kg] (435.35) 664 kJ/kg @ BP
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

h20 = {'M': 18.01528 / 1000,                         # Molar mass [kg/mol]
       'T_e': 293.15,                                # Propellant temperature [K] @BP
       'C_pl': 0,                                    # Liquid phase specific heat [J/kg*K]
       'C_pv': 4181.3,                               # Vapor phase specific heat (constant pressure) [J/kg*K]
       'h_v': 104 * 1000,                            # Heat of vaporization [J/kg]
       'T_v': 373.15,                                # Vaporization temperature [K]
       'R_p': R / (18.01528 / 1000),                 # Specific gas constant
       'p_t': (350+70) * 1.1 * 6894,                 # Propellant tank initial pressure [Pa]
       'a': 0.5536,                                  # van der Wall constant A [Pa*m^6/mol^2]
       'b': 0.00003049,                              # van der Wall constant B [m^3/mol]
       'rho': 999.9720,                              # Density [kg/m^3]
       'p_v': 0,                                     # Operating point vapor pressure [Pa]
       'name': 'h20'
      }

# Rocket Model (sea-level operation)
isp = 246 * 0.90                                     # specific impulse (sea-level, optimistic estimate) [s]
f = 3.2E3                                            # thrust [N]
mdot_t = f/(g_0 * isp)                               # total mass flowrate [kg/s]
chamber_p = 350 * 6.895 * 1000                       # chamber pressure (assumed to be 380 psi currently) [Pa]
loss_factor = 1.15                                   # estimate of line and injector losses
OF = 1.3                                             # mixture ratio
mdot_o = mdot_t / (1 + (1/OF))                       # oxidizer mass flowrate [kg/s]
mdot_f = mdot_t / (1 + OF)                           # fuel mass flowrate [kg/s]
p_i = 101.3E3*2                                      # inlet pressure (currently 1 atm (gauge)) [Pa]
delta_p = chamber_p * loss_factor - p_i              # required pump discharge pressure [Pa]

# barleycorn conversions
g_0 = 32.2
delta_p *= 0.000145038

def imps(prop):
    rho = prop['rho'] * 0.062428
    h_v = prop['p_v'] * 0.000145038 * 144 / rho
    if prop == ipa:
        mdot = mdot_f * 2.20462                      # [lb/s]
    elif prop == lox:
        mdot = mdot_o * 2.20462
    q = mdot / rho                                   # volumetric flowrate [f^3/s]
    h_p = 144 * delta_p / rho                        # required head rise [ft]
    h_i = p_i * 0.000145038 * 144 / rho              # inlet head [ft]
    npsh_a = h_i - h_v                               # Net Positive Suction Head (available) [ft]
    return rho, h_v, mdot, q, h_p, npsh_a

# print("mass flow rate")
# print("%.3f" % imps(ipa)[2], "lbm/s (IPA)")
# print("%.3f" % imps(lox)[2], "lbm/s (LOX)", "\n")
# print("volumetric flow rate")
# print("%.4f" % imps(ipa)[3], "ft^3/s (IPA)")
# print("%.4f" % imps(lox)[3], "ft^3/s (LOX)", "\n")
# print("required pressure head")
# print("%.3f" % imps(ipa)[4], "ft (IPA)")
# print("%.3f" % imps(lox)[4], "ft (LOX)", "\n")
# print("Net Positive Suction Head Available")
# print("%.3f" % imps(ipa)[5], "ft (IPA)")
# print("%.3f" % imps(lox)[5], "ft (LOX)")


#  ------------------------------------------------------------------------------------
#                                impeller calculations
#  ------------------------------------------------------------------------------------

# INPUTS
RPM = 20000                         # Motor speed [rpm]
dC_RPM = 2500                       # Motor RPM Increment
pump_efficiency = 0.40
tip_diameter = 0.12                 # [ft]

# BARSKE IMPELLER DIMENSIONS
head_coefficient = 0.7
flow_coefficient = 0.8
suction_specific_speed = 7500
diffuser_exit_ratio = 3
diffuser_half_angle = 5             # [Deg]
tip_height = 5.1                    # [mm] 3
blade_number = 10
blade_thickness = 3.175             # [mm] 1


# OUTPUTS

def outputs(prop):
    global RPM, pump_efficiency, tip_diameter, head_coefficient, flow_coefficient, \
           suction_specific_speed, diffuser_exit_ratio, diffuser_half_angle, \
           tip_height, blade_number, blade_thickness

    specific_speed = RPM * (imps(prop)[3] * 448.813) ** 0.5 / imps(prop)[4] ** 0.75

    fluid_power = (imps(prop)[2] * 0.453) * (imps(prop)[4] / 3.280) * 9.81 / 1000                   # [kW]

    motor_power_required = fluid_power / pump_efficiency                                            # [kW]

    specific_diameter = (tip_diameter * imps(prop)[4] ** 0.25) / (imps(prop)[3] * 448.813) ** 0.5

    # tip_discharge_speed = imps(prop)[2] * (2 * m.pi / 60) * (tip_diameter / 2)
    # tip_discharge_speed = RPM * (2 * m.pi / 60) * (tip_diameter / 2)
    # head_coefficient_computed = 32.2 * imps(prop)[4] / tip_discharge_speed ** 2

    impeller_diameter = (1300 / (specific_speed * (imps(prop)[4] ** 0.25))) * ((imps(prop)[3] * 448.813) / head_coefficient) ** 0.5

    outlet_diameter = 0.268 * m.sqrt((imps(prop)[3] * 448.813) / flow_coefficient) * (head_coefficient / imps(prop)[4]) ** 0.25

    eye_diameter = 5.1 * ((imps(prop)[3] * 448.813) / RPM) ** 0.333

# ---------------------------------------------------------------------------------------------------------------------

    NPSHR = RPM * (imps(prop)[3] * 448.813) ** 0.5 / suction_specific_speed ** 1.333 + (imps(prop)[3] * 448.813) ** 2 / (386 * eye_diameter ** 4)

    diffuser_exit_diameter = 2 * m.sqrt(diffuser_exit_ratio) * outlet_diameter / 2
    diffuser_length = (diffuser_exit_diameter / 2 - outlet_diameter / 2) / m.tan(diffuser_half_angle * m.pi / 180)

    impeller_eye_area = m.pi * eye_diameter ** 2

    inlet_blade_tip_height = impeller_eye_area / (m.pi * eye_diameter - blade_number * (blade_thickness * 0.03937))

    return specific_speed, fluid_power, motor_power_required, specific_diameter,\
        impeller_diameter, outlet_diameter, eye_diameter, NPSHR, diffuser_exit_diameter, \
        diffuser_length, impeller_eye_area, inlet_blade_tip_height, NPSHR

# print("Specific Speed")
# print("%.2f" % outputs(ipa)[0], " (IPA)")
# print("%.2f" % outputs(lox)[0], " (LOX)", "\n")
# print("Fluid Power")
# print("%.2f" % outputs(ipa)[1], " [kW] (IPA)")
# print("%.2f" % outputs(lox)[1], " [kW] (LOX)", "\n")
# print("Required Motor Power")
# print("%.2f" % outputs(ipa)[2], " [kW] (IPA)")
# print("%.2f" % outputs(lox)[2], " [kW] (LOX)", "\n")
# print("Specific Diameter")
# print("%.3f" % outputs(ipa)[3], " (IPA)")
# print("%.3f" % outputs(lox)[3], " (LOX)", "\n")
# print("Impeller Diameter (D2)")
# print("%.3f" % outputs(ipa)[4], " [in] (IPA)")
# print("%.3f" % outputs(lox)[4], " [in] (LOX)", "\n")
print("NPSHR")
print("%.2f" % outputs(ipa)[7], " (IPA)")
print("%.2f" % outputs(lox)[7], " (LOX)", "\n")

print(tabulate([["RPM", RPM], ["Specific Speed", outputs(lox)[0]], ["Fluid Power [kW]", outputs(lox)[1]],
                ["Required Motor Power [kW]", outputs(lox)[2]], ["Specific Diameter [in]", outputs(lox)[3]],
                ["Impeller Diameter [in]", outputs(lox)[4]], ["Throat Diameter [in]", outputs(lox)[5]],
                ["Eye Diameter [in]", outputs(lox)[6]], ["Impeller Eye Area [in^2]", outputs(lox)[10]],
                ["Inlet blade tip height [in]", 0.0625],["Blade Number", 6.0]],
                ["           LOX", "   "]))
