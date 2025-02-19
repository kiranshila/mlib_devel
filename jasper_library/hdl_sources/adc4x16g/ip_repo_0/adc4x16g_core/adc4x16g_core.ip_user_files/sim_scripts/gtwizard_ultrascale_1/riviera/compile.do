vlib work
vlib riviera

vlib riviera/xpm
vlib riviera/gtwizard_ultrascale_v1_7_7
vlib riviera/xil_defaultlib

vmap xpm riviera/xpm
vmap gtwizard_ultrascale_v1_7_7 riviera/gtwizard_ultrascale_v1_7_7
vmap xil_defaultlib riviera/xil_defaultlib

vlog -work xpm  -sv2k12 \
"C:/Xilinx/Vivado/2019.2/data/ip/xpm/xpm_cdc/hdl/xpm_cdc.sv" \
"C:/Xilinx/Vivado/2019.2/data/ip/xpm/xpm_memory/hdl/xpm_memory.sv" \

vcom -work xpm -93 \
"C:/Xilinx/Vivado/2019.2/data/ip/xpm/xpm_VCOMP.vhd" \

vlog -work gtwizard_ultrascale_v1_7_7  -v2k5 \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_bit_sync.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gte4_drp_arb.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gthe4_delay_powergood.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gtye4_delay_powergood.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gthe3_cpll_cal.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gthe3_cal_freqcnt.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gthe4_cpll_cal.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gthe4_cpll_cal_rx.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gthe4_cpll_cal_tx.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gthe4_cal_freqcnt.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gtye4_cpll_cal.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gtye4_cpll_cal_rx.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gtye4_cpll_cal_tx.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gtye4_cal_freqcnt.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gtwiz_buffbypass_rx.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gtwiz_buffbypass_tx.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gtwiz_reset.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gtwiz_userclk_rx.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gtwiz_userclk_tx.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gtwiz_userdata_rx.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_gtwiz_userdata_tx.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_reset_sync.v" \
"../../../ipstatic/hdl/gtwizard_ultrascale_v1_7_reset_inv_sync.v" \

vlog -work xil_defaultlib  -v2k5 \
"../../../../adc4x16g_core.srcs/sources_1/ip/gtwizard_ultrascale_1/sim/gtwizard_ultrascale_v1_7_gtye4_channel.v" \
"../../../../adc4x16g_core.srcs/sources_1/ip/gtwizard_ultrascale_1/sim/gtwizard_ultrascale_1_gtye4_channel_wrapper.v" \
"../../../../adc4x16g_core.srcs/sources_1/ip/gtwizard_ultrascale_1/sim/gtwizard_ultrascale_v1_7_gtye4_common.v" \
"../../../../adc4x16g_core.srcs/sources_1/ip/gtwizard_ultrascale_1/sim/gtwizard_ultrascale_1_gtye4_common_wrapper.v" \
"../../../../adc4x16g_core.srcs/sources_1/ip/gtwizard_ultrascale_1/sim/gtwizard_ultrascale_1_gtwizard_gtye4.v" \
"../../../../adc4x16g_core.srcs/sources_1/ip/gtwizard_ultrascale_1/sim/gtwizard_ultrascale_1_gtwizard_top.v" \
"../../../../adc4x16g_core.srcs/sources_1/ip/gtwizard_ultrascale_1/sim/gtwizard_ultrascale_1.v" \

vlog -work xil_defaultlib \
"glbl.v"

