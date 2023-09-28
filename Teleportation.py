#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 19:18:09 2023

@author: abdullahalshihry
"""

import qiskit as qs
import qiskit.visualization as qv
import qiskit.quantum_info as qf


qr = qs.QuantumRegister(3)
cr = qs.ClassicalRegister(2)
qc = qs.QuantumCircuit(qr,cr)

x = qf.random_statevector(2)
qc.initialize(x, 0)
qv.plot_bloch_multivector(x)

qc.h(1)
qc.cx(1,2)

qc.cx(0,1)
qc.h(0)



qc.measure([0,1], [0,1])

qc.x(2).c_if(cr[1],1)
qc.z(2).c_if(cr[0],1)

job = qs.execute(qc, qs.Aer.get_backend('statevector_simulator'), shots = 1)
result = job.result().get_statevector()
qv.plot_bloch_multivector(result)


    
qc.draw('mpl')