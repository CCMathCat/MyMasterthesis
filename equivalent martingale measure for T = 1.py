#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Parameter aus dem Modell
delta_S_u = 0.818
delta_S_m = -0.091
delta_S_d = -0.909

# Martingalbedingung:
# q_u * delta_S_u + q_m * delta_S_m + q_d * delta_S_d = 0
# Normierung: q_u + q_m + q_d = 1
# Positivitätsbedingungen: q_u, q_m, q_d >= 0

# Parameterbereich für q_m
q_m_vals = np.linspace(0, 0.9, 500)

# Berechnung der zugehörigen q_u und q_d
q_u_vals = (0.909 - 0.818 * q_m_vals) / 1.727
q_d_vals = 1 - q_u_vals - q_m_vals

# Filtere zulässige Werte: alle q >= 0
valid_mask = (q_u_vals >= 0) & (q_d_vals >= 0)

# Gefilterte Werte
q_m_valid = q_m_vals[valid_mask]
q_u_valid = q_u_vals[valid_mask]
q_d_valid = q_d_vals[valid_mask]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(q_m_valid, q_u_valid, label=r'$q_u$', linewidth=2)
plt.plot(q_m_valid, q_d_valid, label=r'$q_d$', linewidth=2)
plt.plot(q_m_valid, q_m_valid, label=r'$q_m$', linestyle='--', linewidth=1)

plt.xlabel(r'$q_m$', fontsize=14)
plt.ylabel('Probability', fontsize=14)
plt.title('Range of Equivalent Martingale Measures', fontsize=16)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

