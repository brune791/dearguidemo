# from email.policy import default
import dearpygui.dearpygui as dpg
dpg.create_context()

wind_id = dpg.generate_uuid()
temp_id= dpg.generate_uuid()
output_id = dpg.generate_uuid()

#call back functions
def get_windchill():
    wind = dpg.get_value(wind_id)
    temp = dpg.get_value(temp_id)
    windchill = calculate_windcill(wind,temp)
    output = get_output(wind,temp,windchill)
    dpg.set_value(output_id,output)
def calculate_windcill(w,t):
    return 35.74 + 0.6215* t - 35.76 * t - 35.75 * w **0.16 + 0.4275 * t * w**0.16

def get_output(w,t,wc):
    output = "with a windspeed of {} mph".format(w)
    output += "\nand a temperature of {} F".format(t)
    output += "\nthe temperature feels like {} F".format(wc)
    return output
dpg.create_viewport(title='windchill calulator', width= 600,height=300)

with dpg.window(label = "windchill calculator", width=600,height=300):
    dpg.add_text("welcome to the windchill calculator")
    dpg.add_input_int(label="wind speed", width=100,tag=wind_id, min_value=0,min_clamped=True)
    dpg.add_input_int(label = "temperature",width = 100,tag=temp_id,default_value=0,
        max_value=40,max_clamped=True)
    dpg.add_button(label = "calculate", callback = get_windchill)
    dpg.add_button(label = "clear")
    dpg.add_text("", tag=output_id)

    
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()