def init():
    '''
        global variables definition to be used in every other class which includes this file 
    '''
    global on_state            #gui on/off state
    on_state = "OFF"

    global mode                 #operating mode
    mode = "MANUAL"

    global VERT_INBEAM_DEFOULT_VALUE
    VERT_INBEAM_DEFOULT_VALUE = 0

    # global HOR_INBEAM_DEFOULT_VALUE
    # HOR_INBEAM_DEFOULT_VALUE=0

    global VERT_DELTA_DEFOULT_VALUE
    VERT_DELTA_DEFOULT_VALUE = 0

    # global HOR_DELTA_DEFOULT_VALUE
    # HOR_DELTA_DEFOULT_VALUE = 0

    global VERT_HOME_DEFOULT_VALUE
    VERT_HOME_DEFOULT_VALUE = 0

    # global HOR_HOME_DEFOULT_VALUE
    # HOR_HOME_DEFOULT_VALUE = 0
