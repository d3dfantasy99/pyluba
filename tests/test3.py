from pymammotion.mammotion.commands.mammotion_command import LubaCommandProtoBLE, MammotionCommand
from pymammotion.proto.luba_msg import LubaMsg
from pymammotion.utility.constant.device_constant import WorkMode, device_mode

print(WorkMode.MODE_READY)

print(device_mode(3))

print(MammotionCommand().resume_execute_task())
print(LubaMsg().parse(MammotionCommand().resume_execute_task()).nav.todev_taskctrl)
