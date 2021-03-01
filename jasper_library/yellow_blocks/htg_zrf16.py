from .yellow_block import YellowBlock
from clk_factors import clk_factors
from constraints import ClockConstraint, ClockGroupConstraint, PortConstraint, RawConstraint


class htg_zrf16(YellowBlock):
    def initialize(self):
        self.add_source('infrastructure/htg_zrf16_infrastructure.v')
        self.add_source('utils/cdc_synchroniser.vhd')

        self.provides.append(self.clk_src)
        self.provides.append(self.clk_src+'90')
        self.provides.append(self.clk_src+'180')
        self.provides.append(self.clk_src+'270')
        self.provides.append(self.clk_src+'_rst')

        self.provides.append('sys_clk')
        self.provides.append('sys_clk90')
        self.provides.append('sys_clk180')
        self.provides.append('sys_clk270')
        self.provides.append('sys_clk_rst')

    def modify_top(self,top):
        inst = top.get_instance('htg_zrf16', 'htg_zrf16_inst')
        inst.add_port('axil_clk',   'axil_clk')
        inst.add_port('axil_rst',   'axil_rst')
        inst.add_port('axil_rst_n', 'axil_rst_n')

        inst.add_port('M_AXI_araddr', 'M_AXI_araddr', width=40)
        inst.add_port('M_AXI_arprot', 'M_AXI_arprot', width=3)
        inst.add_port('M_AXI_arready', 'M_AXI_arready')
        inst.add_port('M_AXI_arvalid', 'M_AXI_arvalid')
        inst.add_port('M_AXI_awaddr', 'M_AXI_awaddr', width=40)
        inst.add_port('M_AXI_awprot', 'M_AXI_awprot', width=3)
        inst.add_port('M_AXI_awready', 'M_AXI_awready')
        inst.add_port('M_AXI_awvalid', 'M_AXI_awvalid')
        inst.add_port('M_AXI_bready', 'M_AXI_bready')
        inst.add_port('M_AXI_bresp', 'M_AXI_bresp', width=2)
        inst.add_port('M_AXI_bvalid', 'M_AXI_bvalid')
        inst.add_port('M_AXI_rdata', 'M_AXI_rdata', width=32)
        inst.add_port('M_AXI_rready', 'M_AXI_rready')
        inst.add_port('M_AXI_rresp', 'M_AXI_rresp', width=2)
        inst.add_port('M_AXI_rvalid', 'M_AXI_rvalid')
        inst.add_port('M_AXI_wdata', 'M_AXI_wdata', width=32)
        inst.add_port('M_AXI_wready', 'M_AXI_wready')
        inst.add_port('M_AXI_wstrb', 'M_AXI_wstrb', width=4)
        inst.add_port('M_AXI_wvalid', 'M_AXI_wvalid')
        #axi4-lite interface for rfdc core
        inst.add_port('M_AXI_RFDC_araddr', 'M_AXI_RFDC_araddr', width=40)
        inst.add_port('M_AXI_RFDC_arprot', 'M_AXI_RFDC_arprot', width=3)
        inst.add_port('M_AXI_RFDC_arready', 'M_AXI_RFDC_arready')
        inst.add_port('M_AXI_RFDC_arvalid', 'M_AXI_RFDC_arvalid')
        inst.add_port('M_AXI_RFDC_awaddr', 'M_AXI_RFDC_awaddr', width=40)
        inst.add_port('M_AXI_RFDC_awprot', 'M_AXI_RFDC_awprot', width=3)
        inst.add_port('M_AXI_RFDC_awready', 'M_AXI_RFDC_awready')
        inst.add_port('M_AXI_RFDC_awvalid', 'M_AXI_RFDC_awvalid')
        inst.add_port('M_AXI_RFDC_bready', 'M_AXI_RFDC_bready')
        inst.add_port('M_AXI_RFDC_bresp', 'M_AXI_RFDC_bresp', width=2)
        inst.add_port('M_AXI_RFDC_bvalid', 'M_AXI_RFDC_bvalid')
        inst.add_port('M_AXI_RFDC_rdata', 'M_AXI_RFDC_rdata', width=32)
        inst.add_port('M_AXI_RFDC_rready', 'M_AXI_RFDC_rready')
        inst.add_port('M_AXI_RFDC_rresp', 'M_AXI_RFDC_rresp', width=2)
        inst.add_port('M_AXI_RFDC_rvalid', 'M_AXI_RFDC_rvalid')
        inst.add_port('M_AXI_RFDC_wdata', 'M_AXI_RFDC_wdata', width=32)
        inst.add_port('M_AXI_RFDC_wready', 'M_AXI_RFDC_wready')
        inst.add_port('M_AXI_RFDC_wstrb', 'M_AXI_RFDC_wstrb', width=4)
        inst.add_port('M_AXI_RFDC_wvalid', 'M_AXI_RFDC_wvalid')

        inst_infr = top.get_instance('htg_zrf16_infrastructure', 'htg_zrf16_infr_inst')
        if self.clk_src == "arb_clk":
           clkparams = clk_factors(300, self.platform.user_clk_rate)
           inst_infr.add_parameter('GEN_USER_CLK', 1)
           inst_infr.add_parameter('MULTIPLY', clkparams[0])
           inst_infr.add_parameter('DIVIDE',   clkparams[1])
           inst_infr.add_parameter('DIVCLK',   clkparams[2])
        else:
           inst_infr.add_parameter('GEN_USER_CLK', 0)
        inst_infr.add_port('clk_300_p',      "clk_300_p", dir='in',  parent_port=True)
        inst_infr.add_port('clk_300_n',      "clk_300_n", dir='in',  parent_port=True)

        inst_infr.add_port('sys_clk      ', 'sys_clk   ')
        inst_infr.add_port('sys_clk90    ', 'sys_clk90 ')
        inst_infr.add_port('sys_clk180   ', 'sys_clk180')
        inst_infr.add_port('sys_clk270   ', 'sys_clk270')
        inst_infr.add_port('sys_clk_rst', 'sys_rst')

        inst_infr.add_port('user_clk      ', 'arb_clk   ')
        inst_infr.add_port('user_clk90    ', 'arb_clk90 ')
        inst_infr.add_port('user_clk180   ', 'arb_clk180')
        inst_infr.add_port('user_clk270   ', 'arb_clk270')
        inst_infr.add_port('user_clk_rst', 'arb_rst')
		
    def gen_children(self):
        return [YellowBlock.make_block({'fullpath': self.fullpath,'tag': 'xps:sys_block', 'board_id': '20', 'rev_maj': '1', 'rev_min': '0', 'rev_rcs': '1'}, self.platform)]

    def gen_constraints(self):
        cons = []
        cons.append(PortConstraint('clk_300_p', 'clk_300_p'))
        cons.append(ClockConstraint('clk_300_p','clk_300_p', period=3.3333, port_en=True, virtual_en=False, waveform_min=0.0, waveform_max=1.66667))
        if self.clk_src == "arb_clk":
            cons.append(ClockGroupConstraint('-of_objects [get_pins htg_zrf16_infr_inst/user_clk_mmcm_inst/CLKOUT0]', '-of_objects [get_pins htg_zrf16_inst/zynq_ultra_ps_e_0/U0/PS8_i/PLCLK[0]]', 'asynchronous'))
        cons.append(ClockGroupConstraint('-of_objects [get_pins htg_zrf16_infr_inst/sys_clk_mmcm_inst/CLKOUT0]', '-of_objects [get_pins htg_zrf16_inst/zynq_ultra_ps_e_0/U0/PS8_i/PLCLK[0]]', 'asynchronous'))
        #cons.append(ClockGroupConstraint('-of_objects [get_pins htg_zrf16_inst/zynq_ultra_ps_e_0/U0/PS8_i/PLCLK[0]]', '-of_objects [get_pins htg_zrf16_infr_inst/user_clk_mmcm_inst/CLKOUT0]', 'asynchronous'))
        return cons
    def gen_tcl_cmds(self):
        tcl_cmds = {}
        tcl_cmds['pre_synth'] = []
        """
        Add a block design to project with wrapper via its exported tcl script.
        1. Source the tcl script.
        2. Generate the block design via generate_target.
        3. Have vivado make an HDL wrapper around the block design.
        4. Add the wrapper HDL file to project.
        """
        tcl_cmds['pre_synth'] += ['source {}'.format(self.hdl_root + '/infrastructure/htg_zrf16.tcl')]
        tcl_cmds['pre_synth'] += ['generate_target all [get_files [get_property directory [current_project]]/myproj.srcs/sources_1/bd/htg_zrf16/htg_zrf16.bd]']        
        tcl_cmds['pre_synth'] += ['make_wrapper -files [get_files [get_property directory [current_project]]/myproj.srcs/sources_1/bd/htg_zrf16/htg_zrf16.bd] -top']
        tcl_cmds['pre_synth'] += ['add_files -norecurse [get_property directory [current_project]]/myproj.srcs/sources_1/bd/htg_zrf16/hdl/htg_zrf16_wrapper.vhd']
        tcl_cmds['pre_synth'] += ['update_compile_order -fileset sources_1']
        return tcl_cmds