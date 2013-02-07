# -*- coding: utf-8 -*-

import escpos
import exceptions


class ZonerichPrinter(escpos.Escpos):
    """Zonerich Thermal Printer"""
    ### The following command list are for Zonerich Thermal Printers.
    #HW_INIT     = '\x1b\x40'                        #初始化打印机
    
    #CTRL_HT     = '\x09'                            #水平定位，移动打印位置到下一个水平定位点位置
    #CTRL_LF     = '\x0a'                            #打印并走纸，打印缓冲区数据并基于当前的行距向前走纸一行，当前缓冲区为空时只走纸一行
    #CTRL_CR     = '\x0d'                            #打印并回车，打印缓冲区数据但不向前走纸
    #CTRL_END    = '\x00'                            #结束符，有时候可以用到。
    
    #OPEN_DRAW   = '\x1b\x70\x00\x05\x05'            #打开钱箱 '\x10\x14\x01\x01\x08'
    #CUT_PAPER   = '\x1b\x6d'                        #切纸 '\x1b\x69'
    
    #TEXT_ALIGN_LEFT     = '\x1b\x61\x00'            #左对齐方式
    #TEXT_ALIGN_CENTER   = '\x1b\x61\x01'            #居中方式
    #TEXT_ALIGN_RIGHT    = '\x1b\x61\x02'            #右对齐方式
    
    #TEXT_BOLD_ON        = '\x1b\x45\xff'            #打开粗体模式
    #TEXT_BOLD_OFF       = '\x1b\x45\x00'            #关闭粗体模式
    
    #TEXT_LINE_SPACE     = '\x1b\x33'                #设置行间距 0<=N<=255
    #TEXT_CHAR_SPACE     = '\x1b\x41'                #设置字符间距  0<=N<=255
    
    #TEXT_UNDERLINE_ON   = '\x1c\x2d\x01'            #下划线开
    #TEXT_UNDERLINE_OFF  = '\x1c\x2d\x00'            #下划线关
    
    #SET_LEFT_MARGIN     = '\x1d\x4c'                #设置左边距， 0<=nL<=255, 0<=nH<=255
    #SET_PRINT_WIDTH     = '\x1d\x57'                #设置打印宽度， 0<=nL<=255, 0<=nH<=255
    
    #BARCODE_WIDTH       = '\x1d\x77'                #设置条码宽度， N=2，3，4，5，6
    #BARCODE_HEIGHT      = '\x1d\x68'                #设置条码高度， 1<=NM=255
    #BARCODE_EAN8        = '\x1d\x6b\x44'            #打印EAN8格式条码，N=bytes（7～8），  d1...dN
    #BARCODE_EAN13       = '\x1d\x6b\x43'            #打印EAN13格式条码，N=bytes（12～13），  d1...dN
    #BARCODE_CODE39      = '\x1d\x6b\x45'            #打印CODE39格式条码，N=bytes（1～255），  d1...dN
    #BARCODE_CODE128     = '\x1d\x6b\x49'            #打印CODE128格式条码，N=bytes（2～255），  d1...dN
    
    #INVERSE_ON          = '\x1d\x42\xff'            #反白打印开
    #INVERSE_OFF         = '\x1d\x42\x00'            #反白打印关
    #############################################################
    # Feed control sequences
    CTL_LF    = '\x0a'             # Print and line feed
    CTL_FF    = '\x0c'             # Form feed   #TBC
    CTL_CR    = '\x0d'             # Carriage return
    CTL_HT    = '\x09'             # Horizontal tab
    CTL_VT    = '\x0b'             # Vertical tab   #TBC
    # Printer hardware
    HW_INIT   = '\x1b\x40'         # Clear data in buffer and reset modes
    HW_SELECT = '\x1b\x3d\x01'     # Printer select #TBC
    HW_RESET  = '\x1b\x3f\x0a\x00' # Reset printer hardware   #TBC
    # Cash Drawer
    CD_KICK_2 = '\x1b\x70\x00\x05\x05'     # Sends a pulse to pin 2 [] 
    CD_KICK_5 = '\x1b\x70\x01\x05\x05'     # Sends a pulse to pin 5 [] 
    # Paper
    PAPER_FULL_CUT  = '\x1d\x56\x00' # Full cut paper
    PAPER_PART_CUT  = '\x1d\x56\x01' # Partial cut paper
    # Text format   
    TXT_NORMAL      = '\x1b\x21\x00' # Normal text
    TXT_2HEIGHT     = '\x1b\x21\x10' # Double height text
    TXT_2WIDTH      = '\x1b\x21\x20' # Double width text
    TXT_UNDERL_OFF  = '\x1b\x2d\x00' # Underline font OFF
    TXT_UNDERL_ON   = '\x1b\x2d\x01' # Underline font 1-dot ON
    TXT_UNDERL2_ON  = '\x1b\x2d\x02' # Underline font 2-dot ON
    TXT_BOLD_OFF    = '\x1b\x45\x00' # Bold font OFF
    TXT_BOLD_ON     = '\x1b\x45\x01' # Bold font ON
    TXT_FONT_A      = '\x1b\x21\x00' # Font type A
    TXT_FONT_B      = '\x1b\x21\x01' # Font type B
    TXT_ALIGN_LT    = '\x1b\x61\x00' # Left justification
    TXT_ALIGN_CT    = '\x1b\x61\x01' # Centering
    TXT_ALIGN_RT    = '\x1b\x61\x02' # Right justification
    TXT_INVERSE_ON  = '\x1d\x42\xff' #反白打印开
    TXT_INVERSE_OFF = '\x1d\x42\x00' #反白打印关
    
    PAGE_LEFT_MARGIN     = '\x1d\x4c'                #设置左边距， 0<=nL<=255, 0<=nH<=255
    PAGE_PRINT_WIDTH     = '\x1d\x57'                #设置打印宽度， 0<=nL<=255, 0<=nH<=255

    # Barcode format
    BARCODE_HEIGHT  = '\x1d\x68' # Barcode Height [1-255]
    BARCODE_WIDTH   = '\x1d\x77' # Barcode Width  [2-6]
    
    BARCODE_EAN8    = '\x1d\x6b\x44' #打印EAN8格式条码，N=bytes（7～8），  d1...dN
    BARCODE_EAN13   = '\x1d\x6b\x43' #打印EAN13格式条码，N=bytes（12～13），  d1...dN
    BARCODE_CODE39  = '\x1d\x6b\x45' #打印CODE39格式条码，N=bytes（1～255），  d1...dN
    BARCODE_CODE128 = '\x1d\x6b\x49' #打印CODE128格式条码，N=bytes（2～255），  d1...dN

    # Image format  
    S_RASTER_N      = '\x1d\x76\x30\x00' # Set raster image normal size
    S_RASTER_2W     = '\x1d\x76\x30\x01' # Set raster image double width
    S_RASTER_2H     = '\x1d\x76\x30\x02' # Set raster image double height
    S_RASTER_Q      = '\x1d\x76\x30\x03' # Set raster image quadruple
    
    def barcode(self, code,bc, width=None,height=None,pos=None,font=None):
        """Print barcode / Zonerich mode."""
        output = list()
        # Text need to align left when printing barcode. Don't know why...
        output.append(self.TXT_ALIGN_LT)
        # Width
        if width is not None:
            if width >=2 or width <=6:
                output.append(''.join([self.BARCODE_WIDTH,chr(width)]))
            else:
                raise BarcodeSizeError()
        # Height
        if height is not None:
            if height >= 1 or height <=255:
                output.append(''.join([self.BARCODE_HEIGHT,chr(height)]))
            else:
                raise BarcodeSizeError()
        # Font & pos will be ignored.
        
        # Type
        if bc.upper() == "EAN13":
            output.append(self.BARCODE_EAN13)
        elif bc.upper() == "EAN8":
            output.append(self.BARCODE_EAN8)
        elif bc.upper() == "CODE39":
            output.append(self.BARCODE_CODE39)
        elif bc.upper() == "CODE128":
            output.append(self.BARCODE_CODE128)
        else:
            raise BarcodeTypeError()
        # Print Code
        if code:
            code_length = len(code)
            if bc.upper() == "EAN13" and (code_length<12 or code_length>13):
                raise exception.BarcodeCodeError()
            elif bc.upper() == "EAN8" and (code_length<7 or code_length>8):
                raise exception.BarcodeCodeError()
            elif bc.upper() == "CODE39" and (code_length<1 or code_length>255):
                raise exception.BarcodeCodeError()
            elif bc.upper() == "CODE128" and (code_length<2 or code_length>255):
                raise exception.BarcodeCodeError()
            output.append(chr(code_length)) # Zonerich needs the length of code.
            output.append(code)
        else:
            raise exception.BarcodeCodeError()
        # Send the data in one pkt.
        if output:
            self._raw(''.join(output)) # We do send the data to printer once.
            
    def set(self, align=None, font=None, type=None, width=None, height=None):
        #TODO(shenmc): need to test and check if the settings woks or not.
        super(ZonerichPrinter,self).set(align=align,font=font,type=type,width=width,height=height)
    
    def page(self,left_margin=None,print_width=None):
        """Setup page format."""
        output = list()
        if left_margin is not None:
            if not isinstance(left_margin,(list,tuple)) or len(left_margin)<2:
                raise exceptions.Error('Invaid value.')
            if not (1<=left_margin[0]<=255) or not (0<=left_margin[1]<=255):
                raise exceptions.Error('Invaid value.')
            output.append(''.join([self.PAGE_LEFT_MARGIN,chr(left_margin[0]),chr(left_margin[1])]))
        if print_width is not None:
            if not isinstance(print_width,(list,tuple)) or len(print_width)<2:
                raise exceptions.Error('Invaid value.')
            if not (0<=print_width[0]<=255) or not (0<=print_width[1]<=255):
                raise exceptions.Error('Invaid value.')
            output.append(''.join([self.PAGE_PRINT_WIDTH,chr(print_width[0]),chr(print_width[1])]))
        # Send the data in one pkt.
        if output:
            self._raw(''.join(output)) # We do send the data to printer once.
    
    def status(self):
        """Get printer status."""
        pass
    
    def hw(self, hw):
        if not hw or hw.upper() in ('SELECT','RESET'):
            raise exceptions.Error('Not support!')
        super(ZonerichPrinter,self).hw(hw)
    
    def control(self, ctl):
        if not ctl or ctl.upper() in ('FF','VT'):
            raise exceptions.Error('Not support!')
        super(ZonerichPrinter,self).control(ctl)


