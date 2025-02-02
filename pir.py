from dimutils import set_dim, get_dim
from constants import PIR_DIM_DROPOFF_PER_TICK, DIM_MIN, DIM_MAX

def update_dim_and_outputs(new_dim, output_devices):
    set_dim(new_dim)
    for device in output_devices:
        device.update_output()

def check_pir(pir, output_devices):
    pir_value = pir.get_level()
    dim_value = get_dim()
    if dim_value > DIM_MIN and pir_value == 0:
        update_dim_and_outputs(dim_value - PIR_DIM_DROPOFF_PER_TICK, output_devices)
    if dim_value < DIM_MAX and pir_value == 1:
        update_dim_and_outputs(1, output_devices)