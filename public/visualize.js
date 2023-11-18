const { select } = d3;

const width = window.innerWidth;
const height = window.innerHeight;
const nodeRadius = 30;


fetch('/getJsonArray')
  .then(response => response.json())
  .then(data => {
    const jsonArray = data;
    // Use jsonArray in your visualization
    const colorScale = d3.scaleOrdinal(d3.schemeCategory10);

    const svg = select('body').append('svg')
      .attr('width', width)
      .attr('height', height);

    // Create arrow markers
    svg.append('defs')
      .append('marker')
        .attr('id', 'arrowhead')
        .attr('viewBox', '-10 -10 20 20')
        .attr('refX', 20)
        .attr('refY', 0)
        .attr('markerWidth', 20)
        .attr('markerHeight', 20)
        .attr('orient', 'auto')
      .append('path')
        .attr('d', 'M-8,-5 L0,0 L-8,5')
        .attr('fill', 'black');

    // Create edges
    svg.selectAll('line')
      .data(jsonArray.flatMap((sequence, sequenceIndex) => {
        return sequence.slice(0, -1).map((attack, attackIndex) => {
          return {
            source: `${sequenceIndex}-${attackIndex}`,
            target: `${sequenceIndex}-${attackIndex + 1}`
          };
        });
      }))
      .enter().append('line')
        .attr('x1', d => getNodeX(d.source))
        .attr('y1', d => getNodeY(d.source))
        .attr('x2', d => getNodeX(d.target))
        .attr('y2', d => getNodeY(d.target))
        .style('stroke', 'black')
        .style('stroke-width', 3)
        .attr('marker-end', 'url(#arrowhead)');

    // Create nodes
    const nodes = svg.selectAll('circle')
      .data(jsonArray.flatMap((sequence, sequenceIndex) => {
        return sequence.map((attack, attackIndex) => {
          return {
            id: `${sequenceIndex}-${attackIndex}`,
            label: attack.name,
            color: colorScale(attack.name),
          };
        });
      }))
      .enter().append('circle')
        .attr('cx', d => getNodeX(d.id))
        .attr('cy', d => getNodeY(d.id))
        .attr('r', nodeRadius)
        .style('fill', d => d.color)
        .style('stroke', 'black')
        .style('stroke-width', 3);

    // Create labels for nodes
    svg.selectAll('text')
      .data(jsonArray.flatMap((sequence, sequenceIndex) => {
        return sequence.map((attack, attackIndex) => {
          return {
            id: `${sequenceIndex}-${attackIndex}`,
            label: attack.name,
          };
        });
      }))
      .enter().append('text')
        .attr('x', d => getNodeX(d.id))
        .attr('y', d => getNodeY(d.id))
        .attr('dy', 5)
        .attr('text-anchor', 'middle')
        .style('fill', 'black')
        .text(d => d.label);

    // Function to get X coordinate for a node
    function getNodeX(nodeId) {
      const [sequenceIndex, attackIndex] = nodeId.split('-');
      return (parseInt(attackIndex) * 2 + 1) * (width / (jsonArray[parseInt(sequenceIndex)].length * 2));
    }

    // Function to get Y coordinate for a node
    function getNodeY(nodeId) {
      const [sequenceIndex] = nodeId.split('-');
      return ((parseInt(sequenceIndex) + 1) * height) / (jsonArray.length + 1);
    }
  })
  .catch(error => {
    console.error('Error fetching jsonArray:', error);
  });
