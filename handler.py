from analysis.circuit_solver import analyze_circuit
from analysis.thermal_model import thermal_analysis

def handler(event):
    """
    Phoenix AI CATA - Circuit and Thermal Analysis Handler
    Deterministic, math-driven analysis (no LLM required)
    """

    # 1. Validate input
    circuit = event.get("circuit")
    if not circuit:
        return {
            "status": "error",
            "message": "No circuit data provided. Expected JSON describing components and connections."
        }

    try:
        # 2. Run electrical analysis
        electrical_results = analyze_circuit(circuit)

        # 3. Run thermal analysis
        thermal_results = thermal_analysis(electrical_results)

        # 4. Return structured output
        return {
            "status": "completed",
            "electrical_analysis": electrical_results,
            "thermal_analysis": thermal_results
        }

    except Exception as e:
        # 5. Safe error handling
        return {
            "status": "error",
            "message": str(e)
        }
