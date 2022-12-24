import math

def calculate_phi_pn(moment_of_inertia, section_area, kl, steel_modulus_of_elasticity=29000, f_y=50):
        '''        
            This function calculates structural steel column capacity based on moment of inertia, section area,
            unbraced column length (kl), steel_modulus_of_elasticty and steel yield stress (f_y)
        '''        
        radius_of_gyration = math.sqrt(moment_of_inertia/section_area)

        # elastic buckling stress
        if kl == 0:
            kl += 0.00001
        else:
            kl = kl * 12 
    
        f_e = (math.pi)**2 * steel_modulus_of_elasticity / ((kl / radius_of_gyration)**2)
    
        if kl/radius_of_gyration <= (4.71 * (steel_modulus_of_elasticity/f_y)**0.5):
            f_cr = (0.658**(f_y/f_e)) * f_y
        elif kl/radius_of_gyration >= 200:
            f_cr = 0
        else:
            f_cr = 0.8777 * f_e

        phi_pn = int(0.9*section_area*f_cr)
        
        return phi_pn  
    