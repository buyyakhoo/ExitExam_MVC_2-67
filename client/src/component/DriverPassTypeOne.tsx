import { useState } from 'react';

function DriverPassTypeOne() {

    const [handleStatusExam, setHandleStatusExam] = useState<string>("wait");

  return (
    <div>
        {
            handleStatusExam === "wait" ? (
                <button
                    className="px-4 py-2 text-white bg-blue-950 rounded-md hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-blue-800"       
                    onClick={ () => setHandleStatusExam("doing") }
                    >
                    ทดสอบสมรรถนะ
                </button>
            ) : handleStatusExam === "doing" ? (
                <button
                    className="px-4 py-2 text-white bg-blue-950 rounded-md hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-blue-800"       
                    onClick={ () => setHandleStatusExam("done") }
                    >
                    สิ้นสุดการทดสอบ
                </button>
            ) : (
                <p> การทดสอบสำเร็จ </p>
            )
        }
    </div>
  )
}

export default DriverPassTypeOne
