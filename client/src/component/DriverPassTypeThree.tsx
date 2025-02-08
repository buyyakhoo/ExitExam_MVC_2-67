import { useEffect, useState } from 'react';

// interface DriverPassTypeTwoProps {
//     setStatusNewbieSetIn: (status: string) => void;
// }
  
function DriverPassTypeThree() {

    const [random, setRandom] = useState<number>(Math.floor(Math.random() * 10) + 1)
    const [handleTrainingStatus, setHandleTrainingStatus] = useState<string>("wait");
    const [handleAbilityTestStatus, setHandleAbilityTestStatus] = useState<string>("wait");

  return (
    <div className="flex flex-row gap-10 items-center justify-center mt-5">
        {
            random > 5 ? (
                handleTrainingStatus === "wait" ? (
                    <button 
                        className="px-4 py-2 text-white bg-blue-950 rounded-md hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-blue-800" 
                        onClick={() => setHandleTrainingStatus("doing")} >
                            อบรม
                    </button>
                ) : handleTrainingStatus === "doing" ? (
                    <button 
                        className="px-4 py-2 text-white bg-blue-950 rounded-md hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-blue-800" 
                        onClick={() => setHandleTrainingStatus("done")} >
                            สิ้นสุดการอบรม 
                    </button>
                ) : handleTrainingStatus === "done" && handleAbilityTestStatus === "wait" ? (
                    <button 
                        className="px-4 py-2 text-white bg-blue-950 rounded-md hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-blue-800" 
                        onClick={() => setHandleAbilityTestStatus("doing")} > 
                        ทดสอบสมรรถนะ 
                    </button>
                ) : handleTrainingStatus === "done" && handleAbilityTestStatus === "doing" ? (
                    <button 
                        className="px-4 py-2 text-white bg-blue-950 rounded-md hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-blue-800" 
                        onClick={() => setHandleAbilityTestStatus("done")} > 
                        สิ้นสุดการทดสอบ 
                    </button>
                ) : (
                    <p> ทดสอบสมรรถนะสำเร็จ </p>
                )
            ) : (
                handleAbilityTestStatus === "wait" ? (
                    <button 
                        className="px-4 py-2 text-white bg-blue-950 rounded-md hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-blue-800" 
                        onClick={() => setHandleAbilityTestStatus("doing")} > 
                        ทดสอบสมรรถนะ 
                    </button>
                ) :  handleAbilityTestStatus === "doing" ? (
                    <button 
                        className="px-4 py-2 text-white bg-blue-950 rounded-md hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-blue-800" 
                        onClick={() => setHandleAbilityTestStatus("done")} > 
                        สิ้นสุดการทดสอบ 
                    </button>
                ) : (
                    <p> ทดสอบสมรรถนะสำเร็จ </p>
                )
            )
        }
    </div>
  )
}

export default DriverPassTypeThree;
