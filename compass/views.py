from django.shortcuts import render, get_object_or_404, redirect
from .models import Instruction
from .forms import InstructionForm


def index(request):
    if request.method == 'POST':
        form = InstructionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InstructionForm()

    instructions = Instruction.objects.all()
    return render(request, 'compass/index.html', {
        'form': form,
        'instructions': instructions
    })


def instruction_detail(request, instruction_id):
    instruction = get_object_or_404(Instruction, id=instruction_id)
    show_summary = False
    total_distance = 0
    average_risk = 0

    if 'show_summary' in request.GET:
        show_summary = True
        current = instruction
        instructions_in_route = []

        while current:
            instructions_in_route.append(current)
            current = current.previous_instruction

        if instructions_in_route:
            total_distance = sum(inst.distance for inst in instructions_in_route)
            average_risk = sum(inst.risk_level for inst in instructions_in_route) / len(instructions_in_route)

    return render(request, 'compass/instruction_detail.html', {
        'instruction': instruction,
        'show_summary': show_summary,
        'total_distance': total_distance,
        'average_risk': round(average_risk, 2)
    })